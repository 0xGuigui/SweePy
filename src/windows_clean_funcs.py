##
##  windows_clean_funcs.py
##  SweePy
##

from include.imports import glob, os, shutil, win32com
from src.utils import *

def clean_thumbnails():
    if show_confirmation_dialog(message="Voulez-vous vraiment supprimer les miniatures ?"):
        try:
            # Nettoyer les miniatures
            thumbnails_dir = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Windows", "Explorer", "thumbcache_*.db")
            for filename in glob.glob(thumbnails_dir):
                os.remove(filename)
                print(f"Suppression de {filename}")
        except Exception as e:
            show_error_dialog(f"Erreur lors du nettoyage : {str(e)}")

def clean_recycle_bin():
    # try:
    #     # Vider la corbeille en utilisant pywin32
    #     shell = win32com.client.Dispatch("Shell.Application")
    #     recycle_bin = shell.NameSpace(10)
        
    #     # Obtenir les éléments de la corbeille
    #     items = recycle_bin.Items()
        
    #     # Supprimer chaque élément de la corbeille sans confirmation
    #     for item in list(items):
    #         item.InvokeVerb("Delete")
        
    #     print("Corbeille vidée avec succès")
    # except Exception as e:
    #     show_error_dialog(f"Erreur lors du nettoyage de la corbeille : {str(e)}")
    # On vérifie si la corbeille est vide
    try:
        print("Vidage de la corbeille")
        os.system("rd /s /q C:\$Recycle.bin")
    except Exception as e:
        show_error_dialog(f"Erreur lors du nettoyage de la corbeille : {str(e)}")


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
            if os.path.isdir(logs_dir):
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

def clean_temporary_files():
    if show_confirmation_dialog(message="Voulez-vous vraiment supprimer les fichiers temporaires ?"):
        try:
            # Nettoyer les fichiers temporaires (%temp%)
            temp_dir = os.environ["TEMP"]
            for filename in os.listdir(temp_dir):
                file_path = os.path.join(temp_dir, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Suppression de {file_path}")
        except Exception as e:
            show_error_dialog(f"Erreur lors du nettoyage : {str(e)}")

def clean_Windows_Update_files():
    if show_confirmation_dialog(message="Voulez-vous vraiment supprimer les fichiers de mise à jour Windows ?"):
        try:
            # Nettoyer les fichiers de mise à jour Windows
            windir = os.environ["WINDIR"]
            windows_update_dir = os.path.join(windir, "SoftwareDistribution", "Download")
            if os.path.isdir(windows_update_dir):
                shutil.rmtree(windows_update_dir)
                print(f"Suppression de {windows_update_dir}")

        except Exception as e:
            show_error_dialog(f"Erreur lors du nettoyage : {str(e)}")

def clean_prefetch():
    if show_confirmation_dialog(message="Voulez-vous vraiment supprimer les fichiers dans le dossier Prefetch ?"):
        try:
            # Nettoyer les fichiers dans le dossier Prefetch
            windir = os.environ["WINDIR"]
            prefetch_dir = os.path.join(windir, "Prefetch")
            if os.path.isdir(prefetch_dir):
                shutil.rmtree(prefetch_dir)
                print(f"Suppression de {prefetch_dir}")
        except Exception as e:
            show_error_dialog(f"Erreur lors du nettoyage : {str(e)}")