import os
import shutil
import sys
import ctypes
import platform
import glob
import tkinter as tk
from tkinter import messagebox
import winreg
import win32com.client
import pythoncom

def set_console_title():
    ctypes.windll.kernel32.SetConsoleTitleW("PyCleaner v0.2b")

def check_if_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        messagebox.showerror("Erreur", "Erreur lors de la vérification des droits administrateur, le programme est il lancé en tant qu'administrateur ?")
        return False

def check_if_win10_or_higher():
    if platform.release() == "10":
        return True
    else:
        messagebox.showerror("Erreur", "Ce programme ne fonctionne que sur Windows 10 ou supérieur")
        return False

def show_confirmation_dialog(message):
    if "--yesAll" in sys.argv:
        return True
    else:
        result = messagebox.askquestion("Confirmation", message, icon='warning')
        if result == "yes":
            return True
        else:
            return False
    
def show_error_dialog(message):
    messagebox.showerror("Erreur", message)

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
    message = "Voulez-vous vraiment vider la corbeille ?"
    if show_confirmation_dialog(message):
        try:
            # Vider la corbeille en utilisant pywin32
            shell = win32com.client.Dispatch("Shell.Application")
            recycle_bin = shell.NameSpace(10)
            
            # Obtenir les éléments de la corbeille
            items = recycle_bin.Items()
            
            # Supprimer chaque élément de la corbeille
            for item in items:
                item.InvokeVerb("Delete")
            
            print("Corbeille vidée avec succès")
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

def clean_outlook_temporary_files():
    if show_confirmation_dialog(message="Voulez-vous vraiment supprimer les fichiers temporaires d'Outlook ?"):
        try:
            # On ferme Outlook
            os.system("taskkill /f /im outlook.exe")
            print("Fermeture d'Outlook")
            # Nettoyer les fichiers temporaires d'Outlook
            temp_dir = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Windows", "Temporary Internet Files", "Content.Outlook")
            if os.path.isdir(temp_dir):
                shutil.rmtree(temp_dir)
                print(f"Suppression de {temp_dir}")
            # Supprimer le fichier OST d'Outlook
            ost_file = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Outlook", "*.ost")
            for filename in glob.glob(ost_file):
                os.remove(filename)
                print(f"Suppression de {filename}")
            
            messagebox.showinfo("Information", "Pensez a modifier le téléchargement des mails et des pièces jointes dans Outlook à un mois maximum")
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

def clean_downloads():
    if show_confirmation_dialog(message="Voulez-vous vraiment supprimer les fichiers dans le dossier Téléchargements/Downloads au format .exe/.msi/.bat/.tmp ?"):
        try:
            # Nettoyer les fichiers dans le dossier Téléchargements/Downloads au format .exe/.msi/.bat/.tmp
            downloads_dir = os.path.join(os.environ["USERPROFILE"], "Downloads")
            for filename in os.listdir(downloads_dir):
                file_path = os.path.join(downloads_dir, filename)
                if os.path.isfile(file_path):
                    if filename.endswith(".exe") or filename.endswith(".msi") or filename.endswith(".bat") or filename.endswith(".tmp"):
                        os.remove(file_path)
                        print(f"Suppression de {file_path}")
        except Exception as e:
            show_error_dialog(f"Erreur lors du nettoyage : {str(e)}")

def add_this_program_to_windows_defender_exclusion_list():
    try:
        # On récupère le chemin du programme
        program_path = os.path.abspath(sys.argv[0])
        # On ajoute le programme à la liste d'exclusion de Windows Defender
        os.system(f"powershell.exe Add-MpPreference -ExclusionPath '{program_path}'")
        print(f"Ajout de {program_path} à la liste d'exclusion de Windows Defender")
    except Exception as e:
        show_error_dialog(f"Erreur lors de l'ajout du programme à la liste d'exclusion de Windows Defender : {str(e)}")

def clean_windows_defender_cache():
    if show_confirmation_dialog(message="Voulez-vous vraiment supprimer les fichiers dans le cache de Windows Defender ?"):
        try:
            # On désactive Windows Defender
            os.system("powershell.exe Set-MpPreference -DisableRealtimeMonitoring $true")
            print("Désactivation de Windows Defender")

            # Nettoyer les fichiers dans le cache de Windows Defender
            windir = os.environ["WINDIR"]
            defender_cache_dir = os.path.join(windir, "System32", "config", "systemprofile", "AppData", "Local", "Packages", "Microsoft.MicrosoftDefender.AdvancedThreatProtection_8wekyb3d8bbwe", "LocalCache")
            if os.path.isdir(defender_cache_dir):
                shutil.rmtree(defender_cache_dir)
                print(f"Suppression de {defender_cache_dir}")
            # On réactive Windows Defender
            os.system("powershell.exe Set-MpPreference -DisableRealtimeMonitoring $false")
            print("Activation de Windows Defender")
        except Exception as e:
            show_error_dialog(f"Erreur lors du nettoyage : {str(e)}")
            # Vérifier si Windows Defender est activé
            defender_status = os.system("powershell.exe Get-MpPreference | Select RealTimeProtectionEnabled")
            if defender_status == 0:
                # On réactive Windows Defender
                os.system("powershell.exe Set-MpPreference -DisableRealtimeMonitoring $false")
                print("Activation de Windows Defender")

def clean_windows_defender_quarantine():
    if show_confirmation_dialog(message="Voulez-vous vraiment supprimer les fichiers dans la quarantaine de Windows Defender ?"):
        try:
            # On désactive Windows Defender
            os.system("powershell.exe Set-MpPreference -DisableRealtimeMonitoring $true")
            print("Désactivation de Windows Defender")

            # Nettoyer les fichiers dans la quarantaine de Windows Defender
            windir = os.environ["WINDIR"]
            defender_quarantine_dir = os.path.join(windir, "System32", "config", "systemprofile", "AppData", "Local", "Packages", "Microsoft.MicrosoftDefender.AdvancedThreatProtection_8wekyb3d8bbwe", "LocalCache", "Quarantine")
            if os.path.isdir(defender_quarantine_dir):
                shutil.rmtree(defender_quarantine_dir)
                print(f"Suppression de {defender_quarantine_dir}")
            # On réactive Windows Defender
            os.system("powershell.exe Set-MpPreference -DisableRealtimeMonitoring $false")
            print("Activation de Windows Defender")
        except Exception as e:
            show_error_dialog(f"Erreur lors du nettoyage : {str(e)}")
            # Vérifier si Windows Defender est activé
            defender_status = os.system("powershell.exe Get-MpPreference | Select RealTimeProtectionEnabled")
            if defender_status == 0:
                # On réactive Windows Defender
                os.system("powershell.exe Set-MpPreference -DisableRealtimeMonitoring $false")
                print("Activation de Windows Defender")

def clear_browser_cache():
    # On récupère les navigateurs installés
    browsers = []
    # Google Chrome
    if os.path.isdir(os.path.join(os.environ["PROGRAMFILES(X86)"], "Google", "Chrome")):
        browsers.append("Google Chrome")
    # Mozilla Firefox
    if os.path.isdir(os.path.join(os.environ["PROGRAMFILES(X86)"], "Mozilla Firefox")):
        browsers.append("Mozilla Firefox")
    # Microsoft Edge
    if os.path.isdir(os.path.join(os.environ["PROGRAMFILES(X86)"], "Microsoft", "Edge")):
        browsers.append("Microsoft Edge")
    # Internet Explorer
    if os.path.isdir(os.path.join(os.environ["PROGRAMFILES(X86)"], "Internet Explorer")):
        browsers.append("Internet Explorer")
    # Opera
    if os.path.isdir(os.path.join(os.environ["PROGRAMFILES(X86)"], "Opera")):
        browsers.append("Opera")
    
    # On supprime le cache des navigateurs détectés
    for browser in browsers:
        if browser == "Google Chrome":
            try:
                shutil.rmtree(os.path.join(os.environ["LOCALAPPDATA"], "Google", "Chrome", "User Data", "Default", "Cache"))
                print(f"Suppression du cache de Google Chrome")
            except Exception as e:
                show_error_dialog(f"Erreur lors du nettoyage du cache de Google Chrome : {str(e)}")
        elif browser == "Mozilla Firefox":
            try:
                shutil.rmtree(os.path.join(os.environ["LOCALAPPDATA"], "Mozilla", "Firefox", "Profiles", "cache2"))
                print(f"Suppression du cache de Mozilla Firefox")
            except Exception as e:
                show_error_dialog(f"Erreur lors du nettoyage du cache de Firefox: {str(e)}")
        elif browser == "Microsoft Edge":
            try:
                shutil.rmtree(os.path.join(os.environ["LOCALAPPDATA"], "Microsoft", "Edge", "User Data", "Default", "Cache"))
                print(f"Suppression du cache de Microsoft Edge")
            except Exception as e:
                show_error_dialog(f"Erreur lors du nettoyage du cache de Microsoft Edge: {str(e)}")
        elif browser == "Internet Explorer":
            try:
                os.system("RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 8")
                print(f"Suppression du cache d'Internet Explorer")
            except Exception as e:
                show_error_dialog(f"Erreur lors du nettoyage du cache d'Internet Explorer (Utilisez Microsoft Edge): {str(e)}")
        elif browser == "Opera":
            try:
                shutil.rmtree(os.path.join(os.environ["APPDATA"], "Opera Software", "Opera Stable", "Cache"))
                print(f"Suppression du cache d'Opera")
            except Exception as e:
                show_error_dialog(f"Erreur lors du nettoyage du cache d'Opéra: {str(e)}")


def main():

    # Définir le titre de la console
    set_console_title()
    
    # Récupérer l'espace disque avant le nettoyage
    disk_usage_before = shutil.disk_usage(os.environ["SYSTEMDRIVE"])

    # Vérifier si le programme est lancé en tant qu'administrateur
    check_if_admin()

    # Vérifier si le programme est lancé sur Windows 10 ou supérieur
    if not check_if_win10_or_higher():
        sys.exit()

    # Nettoyage des fichiers temporaires (%temp%)
    clean_temporary_files()
    clean_Windows_Update_files()
    clean_thumbnails()
    clean_recycle_bin()
    clean_language_resources()
    clean_logs()
    clean_windows_update_delivery_optimization()
    clean_error_reports()
    clean_directx_shader_cache()
    clean_outlook_temporary_files()
    clean_prefetch()
    clean_downloads()
    add_this_program_to_windows_defender_exclusion_list()
    clean_windows_defender_cache()
    clean_windows_defender_quarantine()
    clear_browser_cache()

    # Get the actual disk usage
    disk_usage_after = shutil.disk_usage(os.environ["SYSTEMDRIVE"])

    # Calculer l'espace libéré en Go
    cleaned_size_gb = round((disk_usage_after.free - disk_usage_before.free) / 1024 / 1024 / 1024, 2)

    ctypes.windll.user32.MessageBoxW(0, f"Nettoyage terminé. Espace libéré : {cleaned_size_gb} Go", "Terminé", 0)

if __name__ == "__main__":
    main()
