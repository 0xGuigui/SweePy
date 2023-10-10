from include.imports import ctypes, os, sys, messagebox, shutil, glob
from src.utils import *
from src.windows_clean_funcs import *
from src.wd_clean_funcs import *

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

            # On redémarre explorer.exe
            print("Redémarrage de explorer.exe")
            os.system("start explorer.exe")
            # On redémarre Outlook
            print("Redémarrage de Outlook")
            os.system("start outlook.exe")
            messagebox.showinfo("Information", "Pensez a modifier le téléchargement des mails et des pièces jointes dans Outlook à un mois maximum")
            # On arrete explorer.exe
            print("Arrêt de explorer.exe")
            os.system("taskkill /f /im explorer.exe")
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
    
    try:
        # Supprimer ce dossier IE Cache des applications UWP
        shutil.rmtree(os.path.join(os.environ["LOCALAPPDATA"], "Microsoft", "Windows", "INetCache", "IE"))
        print(f"Suppression du cache d'Internet Explorer")
    except Exception as e:
        show_error_dialog(f"Erreur lors du nettoyage du cache d'Internet Explorer: {str(e)}")



def main():

    # Définir le titre de la console
    set_console_title()

    # On arrête explorer.exe
    print("Arrêt de explorer.exe")
    os.system("taskkill /f /im explorer.exe")

    # Récupérer l'espace disque avant le nettoyage
    disk_usage_before = shutil.disk_usage(os.environ["SYSTEMDRIVE"])

    # Vérifier si le programme est lancé en tant qu'administrateur
    check_if_program_is_started_with_admin_rights()

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

    # On redémarre explorer.exe
    print("Redémarrage de explorer.exe")
    os.system("start explorer.exe")

    # Get the actual disk usage
    disk_usage_after = shutil.disk_usage(os.environ["SYSTEMDRIVE"])

    # Calculer l'espace libéré en Go
    cleaned_size_gb = round((disk_usage_after.free - disk_usage_before.free) / (1024 ** 3), 2)

    # Si cleaned_size_gb est négatif, on le met à 0
    if cleaned_size_gb < 0:
        cleaned_size_gb = 0

    ctypes.windll.user32.MessageBoxW(0, f"Nettoyage terminé. Espace libéré : {cleaned_size_gb} Go", "Terminé", 0)

if __name__ == "__main__":
    main()
