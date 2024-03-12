##
##  others_cleans.py
##  SweePy
##

from src.utils import *
from include.imports import os, shutil, glob

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


def clean_outlook_temporary_files(username):
    if show_confirmation_dialog(message="Voulez-vous vraiment supprimer les fichiers temporaires d'Outlook ?"):
        try:
            # On vérifie si Outlook est installé
            if os.path.isdir(os.path.join(os.environ["PROGRAMFILES"], "Microsoft Office", "root", "Office16")):
                # On ferme Outlook
                os.system("taskkill /f /im outlook.exe")
                print("Fermeture d'Outlook")

                # On supprime les fichiers temporaires d'Outlook
                outlook_temp_path = os.path.join("C:\\Users", username, "AppData", "Local", "Microsoft", "Outlook", "Temp")
                if os.path.isdir(outlook_temp_path):
                    shutil.rmtree(outlook_temp_path)
                    print("Suppression des fichiers temporaires d'Outlook")

                # Nettoyer les fichiers temporaires d'Outlook
                outlook_temp_path = os.path.join("C:\\Users", username, "AppData", "Local", "Microsoft", "Windows", "Temporary Internet Files", "Content.Outlook")
                if os.path.isdir(outlook_temp_path):
                    shutil.rmtree(outlook_temp_path)
                    print("Suppression des fichiers temporaires d'Outlook")

                # Supprimer les fichiers OST d'Outlook
                outlook_temp_path = os.path.join("C:\\Users", username, "AppData", "Local", "Microsoft", "Outlook")
                for filename in glob.glob(os.path.join(outlook_temp_path, "*.ost")):
                    os.remove(filename)
                    print(f"Suppression de {filename}")

                
                
                # On redémarre Outlook
                print("Redémarrage de Outlook")
                os.system("start outlook.exe")
                messagebox.showinfo("Information", "Pensez a modifier le téléchargement des mails et des pièces jointes dans Outlook à un mois maximum")

            else:
                print("Outlook n'est pas installé")
        except Exception as e:
            show_error_dialog(f"Erreur lors du nettoyage : {str(e)}")