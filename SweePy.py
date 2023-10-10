from include.imports import ctypes, os, sys, messagebox, shutil, glob, windows_clean_funcs, wd_clean_funcs, others_clean_funcs
from src.utils import *
from src.windows_clean_funcs import *
from src.wd_clean_funcs import *

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

    # Appel des bouches de netttoyage
    windows_clean_funcs()
    others_clean_funcs()
    wd_clean_funcs()

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
