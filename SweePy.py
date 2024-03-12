##
##  SweePy.py
##  SweePy
##

from include.imports import ctypes, os, sys, messagebox, shutil, glob, windows_clean_funcs, wd_clean_funcs, others_clean_funcs, delete_elements_from_config
from src.utils import *
from src.windows_clean_funcs import *
from src.wd_clean_funcs import *
from tkinter import Tk, messagebox, simpledialog

def main():
    version = "0.2.4"

    # Vérifier si le programme est lancé en tant qu'administrateur
    # check_if_program_is_started_with_admin_rights()

    # Récupérer le nom d'utilisateur

    # Information developer
    print("Développé par : 0xGuigui")
    print(f"Version : {version}")
    print("GitHub : https://github.com/0xGuigui")

    username = ""

    # Créer une fenêtre tkinter invisible
    root = Tk()
    root.withdraw()

    # Demander si c'est un utilisateur ou un administrateur qui utilise le programme
    if ctypes.windll.shell32.IsUserAnAdmin() == 0:
        user_type = messagebox.askquestion("Type d'utilisateur", "Êtes-vous un administrateur?")
        if user_type == 'yes':
            # Demander des permissions admin
            if not is_admin():
                set_console_title(version)
                save_userloggedin()
                username = get_userloggedin()
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                sys.exit(0)
        else:
            set_console_title(version)
            save_userloggedin()
            username = get_userloggedin()
            print("L'utilisateur est un utilisateur normal.")


    # Demander si l'utilisateur veut passer toutes les demandes de vérification de nettoyage
    skip_confirmation = messagebox.askquestion("Passer toutes les demandes de vérification de nettoyage", "Voulez-vous passer toutes les demandes de vérification de nettoyage?")
    if skip_confirmation == 'yes':
        sys.argv.append("--yesAll")

    # On arrête explorer.exe
    print("Arrêt de explorer.exe")
    os.system("taskkill /f /im explorer.exe" if os.name == "nt" else "pkill explorer")

    # Récupérer l'espace disque avant le nettoyage
    disk_usage_before = shutil.disk_usage(os.environ["SYSTEMDRIVE"])

    # Vérifier si le programme est lancé sur Windows 10 ou supérieur
    if not check_if_win10_or_higher():
        sys.exit()

    # Appel des bouches de netttoyage
    windows_clean_funcs(username)
    others_clean_funcs(username)
    # delete_elements_from_config(config.cfg)
    # wd_clean_funcs()

    # On redémarre explorer.exe
    print("Redémarrage de explorer.exe")
    if ctypes.windll.shell32.IsUserAnAdmin():
        # Créer un fichier batch pour redémarrer explorer.exe
        with open(r"C:\Users\Public\SweePy\restart_explorer.bat", "w") as file:
            file.write("start explorer.exe")
            # Exécuter le fichier batch
            os.system(r"C:\Users\Public\SweePy\restart_explorer.bat")
    else:
        # Exécuter explorer.exe normalement
        os.system("start explorer.exe")

    # delete SweePy folder in Public
    if os.path.exists(os.path.join(os.environ["PUBLIC"], "SweePy")):
        shutil.rmtree(os.path.join(os.environ["PUBLIC"], "SweePy"))
        print("Dossier SweePy supprimé")

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
