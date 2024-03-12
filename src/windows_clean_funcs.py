##
##  windows_clean_funcs.py
##  SweePy
##

from include.imports import glob, os, shutil, win32com, ctypes
from src.utils import *
import winshell
import re

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def clean_thumbnails(username):
    if show_confirmation_dialog(message="Voulez-vous vraiment supprimer les miniatures ?"):
        try:
            # Nettoyer les miniatures
            thumbnails_dir = os.path.join("C:\\Users", username, "AppData", "Local", "Microsoft", "Windows", "Explorer", "thumbcache*")
            for filename in glob.glob(thumbnails_dir):
                os.remove(filename)
                print(f"Suppression de {filename}")
        except Exception as e:
            show_error_dialog(f"Erreur lors du nettoyage : {str(e)}")

def clean_recycle_bin():
    if show_confirmation_dialog(message="Voulez-vous vraiment vider la corbeille ?"):
        try:
            winshell.recycle_bin().empty(confirm=False,
                show_progress=False, sound=True)
            print("La corbeille a été vidée avec succès!")
        except:
            print("La corbeille est déjà vide!")

def clean_language_resources():
    if show_confirmation_dialog(message="Voulez-vous vraiment supprimer les fichiers de ressources langue ?"):
        try:
            # Nettoyer les fichiers de ressources langue
            windir = os.environ["WINDIR"]
            resources_dir = os.path.join(windir, "WinSxS", "ManifestCache")
            if os.path.isdir(resources_dir):
                shutil.rmtree(resources_dir)
                print(f"Suppression de {resources_dir}")
        except Exception as e:
            show_error_dialog(f"Erreur lors du nettoyage : {str(e)}")

def clean_logs():
    if show_confirmation_dialog(message="Voulez-vous vraiment supprimer les fichiers de logs ?"):
        try:
            # Nettoyer les fichiers de logs
            windir = os.environ["WINDIR"]
            logs_dir = os.path.join(windir, "Logs")

            # Vérifier si le répertoire CBS est présent dans logs_dir
            if os.path.isdir(logs_dir):
                for dirpath, dirnames, filenames in os.walk(logs_dir):
                    for dirname in dirnames:
                        if re.match(r"^CBS$", dirname, re.IGNORECASE):
                            print(f"Ignoré le répertoire CBS: {os.path.join(dirpath, dirname)}")
                            dirnames.remove(dirname)  # Ne pas descendre dans le répertoire CBS

                shutil.rmtree(logs_dir)
                print(f"Suppression de {logs_dir}")
        except Exception as e:
            show_error_dialog(f"Erreur lors du nettoyage : {str(e)}")

def clean_windows_update_delivery_optimization():
    if show_confirmation_dialog(message="Voulez-vous vraiment supprimer les fichiers d'optimisation de livraison des mise à jour Windows ?"):
        try:
            # Nettoyer les fichiers d'optimisation de livraison des mise à jour Windows
            windir = os.environ["WINDIR"]
            delivery_optimization_dir = os.path.join(windir, "System32", "DeliveryOptimization")
            if os.path.isdir(delivery_optimization_dir):
                shutil.rmtree(delivery_optimization_dir)
                print(f"Suppression de {delivery_optimization_dir}")
        except Exception as e:
            show_error_dialog(f"Erreur lors du nettoyage : {str(e)}")

def clean_error_reports():
    if show_confirmation_dialog(message="Voulez-vous vraiment supprimer les fichiers de rapport d'erreur ?"):
        try:
            # Nettoyer les fichiers de rapport d'erreur
            windir = os.environ["WINDIR"]
            error_reports_dir = os.path.join(windir, "System32", "config", "systemprofile", "AppData", "Local", "Microsoft", "Windows", "WER", "ReportArchive")
            if os.path.isdir(error_reports_dir):
                shutil.rmtree(error_reports_dir)
                print(f"Suppression de {error_reports_dir}")
        except Exception as e:
            show_error_dialog(f"Erreur lors du nettoyage : {str(e)}")

def clean_directx_shader_cache():
    if show_confirmation_dialog(message="Voulez-vous vraiment supprimer les fichiers de Shader Cache DirectX ?"):
        try:
            # Nettoyer les fichiers de Shader Cache DirectX
            windir = os.environ["WINDIR"]
            shader_cache_dir = os.path.join(windir, "Temp", "DxShaderCache")
            if os.path.isdir(shader_cache_dir):
                shutil.rmtree(shader_cache_dir)
                print(f"Suppression de {shader_cache_dir}")
        except Exception as e:
            show_error_dialog(f"Erreur lors du nettoyage : {str(e)}")

def clean_temporary_files(username):
    if show_confirmation_dialog(message="Voulez-vous vraiment supprimer les fichiers temporaires ?"):
        try:
            # Nettoyer les fichiers temporaires dans Appdata / Local / Temp
            temp_dir = os.path.join("C:\\Users", username, "AppData", "Local", "Temp")
            if os.path.isdir(temp_dir):
                shutil.rmtree(temp_dir)
                print(f"Suppression de {temp_dir}")
        except Exception as e:
            show_error_dialog(f"Erreur lors du nettoyage : {str(e)}")

    # delete SweePy folder in Public
    if os.path.exists(os.path.join(os.environ["PUBLIC"], "SweePy")):
        shutil.rmtree(os.path.join(os.environ["PUBLIC"], "SweePy"))
        print("Dossier SweePy supprimé")

# Admin rights required
def clean_Windows_Update_files():
    if ctypes.windll.shell32.IsUserAnAdmin() == 0:
        print("Nettoyage des fichiers de mise à jour Windows nécessite des droits d'administrateur")
        return
    if show_confirmation_dialog(message="Voulez-vous vraiment supprimer les fichiers de mise à jour Windows ?"):
        try:
            # Get the Windows directory
            windir = os.path.expandvars("%WINDIR%")
            windows_update_dir = os.path.join(windir, "SoftwareDistribution", "Download")

            # Check if the directory exists
            if os.path.isdir(windows_update_dir):
                # Delete the directory
                shutil.rmtree(windows_update_dir)
                print(f"Suppression de {windows_update_dir}")

                # Recreate the directory
                os.makedirs(windows_update_dir)
                print(f"Recreation de {windows_update_dir}")

        except Exception as e:
            show_error_dialog(f"Erreur lors du nettoyage : {str(e)}")


# Admin rights required
def clean_prefetch():
    if ctypes.windll.shell32.IsUserAnAdmin() == 0:
        print("Nettoyage du dossier Prefetch nécessite des droits d'administrateur")
        return
    if show_confirmation_dialog(message="Voulez-vous vraiment supprimer les fichiers dans le dossier Prefetch ?"):
        try:
            # Get the Windows directory
            windir = os.path.expandvars("%WINDIR%")
            prefetch_dir = os.path.join(windir, "Prefetch")

            # Check if the directory exists
            if os.path.isdir(prefetch_dir):
                # Delete the directory
                shutil.rmtree(prefetch_dir)
                print(f"Suppression de {prefetch_dir}")

                # Recreate the directory
                os.makedirs(prefetch_dir)
                print(f"Recreation de {prefetch_dir}")

        except Exception as e:
            show_error_dialog(f"Erreur lors du nettoyage : {str(e)}")