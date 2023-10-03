import os
import subprocess
import ctypes
import tkinter as tk
from tkinter import messagebox
import platform
import psutil

bypass_confirmation = False

def is_windows_10_or_higher():
    try:
        # Obtenez la version de Windows
        version_info = platform.win32_ver()

        # Vérifiez si la version est Windows 10 ou supérieure
        major_version = int(version_info[0])
        if major_version >= 10:
            return True
        else:
            return False
    except Exception as e:
        return False
    
if is_windows_10_or_higher():
    print("Le programme est compatible avec Windows 10 ou supérieur.")
else:
    print("Le programme n'est pas compatible avec cette version de Windows ou s'exécute sur un autre système.")

espace_initial = 0

# Nettoyage des fichiers de Windows Update
def clean_windows_update():
    if messagebox.askyesno("Confirmation", "Voulez-vous nettoyer Windows Update ?"):
        print("Cleaning Windows Update...")

        print("Stopping services...")
        try:
            os.system("net stop wuauserv")
            os.system("net stop bits")
            os.system("net stop dosvc")
            os.system("net stop appidsvc")
            os.system("net stop cryptsvc")
        except:
            print("Failed to stop services.")
            return
        print("Services stopped.")

        print("Cleaning Windows Update...")
        try:
            os.system("DISM.exe /Online /Cleanup-image /StartComponentCleanup /ResetBase")
            os.system("DISM.exe /Online /Cleanup-Image /SPSuperseded")
        except:
            print("Failed to clean Windows Update.")
            return
        print("Windows Update cleaned.")

        print("Starting services...")
        try:
            os.system("net start wuauserv")
            os.system("net start bits")
            os.system("net start dosvc")
            os.system("net start appidsvc")
            os.system("net start cryptsvc")
        except:
            print("Failed to start services.")
            return
        print("Services started.")
        pass


# Nettoyage de Windows Defender + Scan AT
def clean_windows_defender():
    if messagebox.askyesno("Confirmation", "Voulez-vous nettoyer Windows Defender ?"):
        print("Cleaning Windows Defender...")

        print("Scanning system, please wait...")
        try:
            os.system("powershell.exe -command \"Start-MpScan -ScanType QuickScan\"")
        except:
            print("Failed to scan system.")
            return
        print("Scan complete.")

        print("Removing threats...")
        try:
            os.system("powershell.exe -command \"Remove-MpThreat -All -Force\"")
        except:
            print("Failed to remove threats.")
            return
        print("Threats removed.")


        print("Disabling Windows Defender...")
        try:
            os.system("powershell.exe -command \"Set-MpPreference -DisableRealtimeMonitoring 0\"")
        except:
            print("Failed to disable Windows Defender.")
            return
        print("Windows Defender disabled.")


        print("Killing Windows Defender processes...")
        try:
            os.system("powershell.exe -command \"Stop-Process -Name MsMpEng -Force\"")
        except:
            print("Failed to kill Windows Defender processes.")
            return
        print("Windows Defender processes killed.")


        print("Cleaning Windows Defender...")
        try:
            os.system("powershell.exe Remove-Item -Path 'C:\\ProgramData\\Microsoft\\Windows Defender\\Scans\\History\\Service\\*' -Verbose")
            os.system("powershell.exe Remove-Item -Path 'C:\\ProgramData\\Microsoft\\Windows Defender\\Scans\\History\\Quick\\*' -Verbose")
            os.system("powershell.exe Remove-Item -Path 'C:\\ProgramData\\Microsoft\\Windows Defender\\Scans\\History\\Full\\*' -Verbose")
            os.system("powershell.exe Remove-Item -Path 'C:\\ProgramData\\Microsoft\\Windows Defender\\Scans\\History\\Custom\\*' -Verbose")
            os.system("powershell.exe Remove-Item -Path 'C:\\ProgramData\\Microsoft\\Windows Defender\\Scans\\History\\Remediation\\*' -Verbose")
        except:
            print("Failed to clean Windows Defender.")
            return
        print("Windows Defender cleaned.")


        print("Re-enabling Windows Defender...")
        try:
            os.system("powershell.exe -command \"Set-MpPreference -DisableRealtimeMonitoring 1\"")
        except:
            print("Failed to re-enable Windows Defender.")
            return
        print("Windows Defender re-enabled.")


        print("Restarting Windows Defender processes...")
        try: 
            os.system("powershell.exe -command \"Start-Process -FilePath 'C:\\Program Files\\Windows Defender\\MSASCui.exe'\"")
            os.system("powershell.exe -command \"Start-Process -FilePath 'C:\\Program Files\\Windows Defender\\MSASCuiL.exe'\"")
        except:
            print("Failed to restart Windows Defender processes.")
            return
        print("Windows Defender processes restarted.")
        pass
    

# Nettoyage des fichiers temporaires
def clean_temporary_files():
    if messagebox.askyesno("Confirmation", "Voulez-vous nettoyer les fichiers temporaires ?"):
        print("Cleaning temporary files...")
        try:
            os.system("powershell.exe -command \"Remove-Item -Path 'C:\\Windows\\Temp\\*' -Force -Recurse -Verbose\"")
            os.system("powershell.exe -command \"Remove-Item -Path 'C:\\Users\\%USERNAME%\\AppData\\Local\\Temp\\*' -Force -Recurse -Verbose\"")
        except:
            print("Failed to clean temporary files.")
            return
        print("Temporary files cleaned.")
        pass


# Nettoyage de la corbeille
def clean_recycle_bin():
    if messagebox.askyesno("Confirmation", "Voulez-vous nettoyer la corbeille ?"):
        print("Cleaning recycle bin...")
        try:
            os.system("powershell.exe -command \"Clear-RecycleBin -Force\"")
        except:
            print("Failed to clean recycle bin.")
            return
        print("Recycle bin cleaned.")
        pass

# Nettoyage des fichiers journaux de la mise a jour Windows
def clean_windows_update_logs():
    if messagebox.askyesno("Confirmation", "Voulez-vous nettoyer les fichiers journaux de la mise à jour Windows ?"):
        print("Cleaning Windows Update logs...")
        try:
            os.system("powershell.exe -command \"Remove-Item -Path 'C:\\Windows\\Logs\\WindowsUpdate\\*' -Force -Recurse -Verbose\"")
        except:
            print("Failed to clean Windows Update logs.")
            return
        print("Windows Update logs cleaned.")
        pass

# Nettoyage des fichiers journaux de Windows
def clean_windows_logs():
    if messagebox.askyesno("Confirmation", "Voulez-vous nettoyer les fichiers journaux de Windows ?"):
        print("Cleaning Windows logs...")
        try:
            os.system("powershell.exe -command \"Remove-Item -Path 'C:\\Windows\\Logs\\*' -Force -Recurse -Verbose\"")
        except:
            print("Failed to clean Windows logs.")
            return
        print("Windows logs cleaned.")
        pass


# Detection du dossier de téléchargement (Downloads ou Téléchargements)
def check_user_downloads_folder():
    # Obtenez le nom d'utilisateur de l'utilisateur actuel
    username = os.getlogin()

    # Vérifiez si le dossier "Downloads" existe dans le répertoire de l'utilisateur
    downloads_path = os.path.join("C:\\Users", username, "Downloads")
    if os.path.exists(downloads_path) and os.path.isdir(downloads_path):
        return downloads_path

    # Vérifiez si le dossier "Téléchargements" existe dans le répertoire de l'utilisateur
    french_downloads_path = os.path.join("C:\\Users", username, "Téléchargements")
    if os.path.exists(french_downloads_path) and os.path.isdir(french_downloads_path):
        return french_downloads_path

# Nettoyage des fichiers téléchargés isntallables .exe, .msi
def clean_downloaded_files():
    if messagebox.askyesno("Confirmation", "Voulez-vous nettoyer les fichiers téléchargés (Programmes d'installation)?"):
        print("Detecting Downloads folder...")
        downloads_folder = check_user_downloads_folder()
        if downloads_folder is None:
            print("Failed to detect Downloads folder.")
            return
        print("Downloads folder detected.")

        print("Cleaning downloaded files...")
        try:
            os.system("powershell.exe -command \"Remove-Item -Path '" + downloads_folder + "\\*.exe' -Force -Recurse -Verbose\"")
            os.system("powershell.exe -command \"Remove-Item -Path '" + downloads_folder + "\\*.msi' -Force -Recurse -Verbose\"")
        except:
            print("Failed to clean downloaded files.")
            return
        print("Downloaded files cleaned.")
        pass

# Nettoyage des fichiers Internet temporaires
def clean_internet_temporary_files():
    if messagebox.askyesno("Confirmation", "Voulez-vous nettoyer les fichiers Internet temporaires ?"):
        print("Cleaning Internet temporary files...")
        try:
            os.system("powershell.exe -command \"Remove-Item -Path 'C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Windows\\INetCache\\*' -Force -Recurse -Verbose\"")
        except:
            print("Failed to clean Internet temporary files.")
            return
        print("Internet temporary files cleaned.")
        pass

# Nettoyage des fichiers de vidange mémoire d'erreur système
def clean_system_error_memory_dump_file():
    if messagebox.askyesno("Confirmation", "Voulez-vous nettoyer les fichiers de vidange mémoire d'erreur système ?"):
        print("Cleaning system error memory dump files...")
        try:
            os.system("powershell.exe -command \"Remove-Item -Path 'C:\\Windows\\*.dmp' -Force -Recurse -Verbose\"")
        except:
            print("Failed to clean system error memory dump files.")
            return
        print("System error memory dump files cleaned.")
        pass

# Nettoyage des des fichiers de ressource linguistique
def clean_language_resource_files():
    if messagebox.askyesno("Confirmation", "Voulez-vous nettoyer les fichiers de ressource linguistique ?"):
        print("Cleaning language resource files...")
        try:
            os.system("powershell.exe -command \"Remove-Item -Path 'C:\\Windows\\SoftwareDistribution\\Download\\*' -Force -Recurse -Verbose\"")
        except:
            print("Failed to clean language resource files.")
            return
        print("Language resource files cleaned.")
        pass    

# Nettoyage des fichiers d'installation temporaires de Windows
def clean_windows_temporary_installation_files():
    if messagebox.askyesno("Confirmation", "Voulez-vous nettoyer les fichiers d'installation temporaires de Windows ?"):
        print("Cleaning Windows temporary installation files...")
        try:
            # Faut supprimer le dossier Windows10Upgrade
            os.system("powershell.exe -command \"Remove-Item -Path 'C:\\Windows\\10Upgrade\\*' -Force -Recurse -Verbose\"")
            os.system("powershell.exe -command \"Remove-Item -Path 'C:\\Windows\\Panther\\*' -Force -Recurse -Verbose\"")
        except:
            print("Failed to clean Windows temporary installation files.")
            return
        print("Windows temporary installation files cleaned.")
        pass

# Fonction pour mesurer l'espace disque utilisé
def get_disk_space_used():
    try:
        disk = psutil.disk_usage('/')
        return disk.used / (1024 * 1024)  # Convertir en Mo
    except Exception as e:
        print("Failed to get disk space used.")
        return 0


def main():

    global espace_initial
    espace_initial = get_disk_space_used()

    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Information", "Le programme va nettoyer votre ordinateur, veuillez ne pas l'éteindre.")

    if is_windows_10_or_higher():
        clean_windows_update()
        clean_windows_defender()
        clean_temporary_files()
        clean_recycle_bin()
        clean_windows_update_logs()
        clean_windows_logs()
        clean_downloaded_files()
        clean_internet_temporary_files()
        clean_system_error_memory_dump_file()
        clean_language_resource_files()
        clean_windows_temporary_installation_files()



    else:
        messagebox.showerror("Erreur", "Le programme n'est pas compatible avec cette version de Windows ou s'exécute sur un autre système.")
    
    espace_final = get_disk_space_used()
    espace_liberer = espace_initial - espace_final
    espace_liberer_giga = espace_liberer / 1024
    espace_liberer_giga_arrondi = round(espace_liberer_giga, 2)
    
    messagebox.showinfo("Information", f"Le nettoyage est terminé. Espace disque libéré : {espace_liberer_giga_arrondi} Go")
    root.destroy()

if __name__ == "__main__":
    main()


# @TODO: Nettoyer Outlook

