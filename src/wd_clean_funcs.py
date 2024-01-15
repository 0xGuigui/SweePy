##
##  wd_clean_funcs.py
##  SweePy
##

from include.imports import os, shutil, sys
from src.utils import *

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