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
import win32con
import pythoncom
from src.windows_clean_funcs import *
from src.wd_clean_funcs import *
from src.utils import *
from src.others_clean import *
from src.custom_delete import *



def windows_clean_funcs(username):
    # On récupère les fonctions de nettoyage
    clean_funcs = [lambda: clean_thumbnails(username), clean_recycle_bin, clean_language_resources, clean_logs, clean_windows_update_delivery_optimization, clean_error_reports, clean_directx_shader_cache, clean_prefetch, clean_Windows_Update_files, lambda: clean_temporary_files(username)]
    # On exécute les fonctions de nettoyage
    for func in clean_funcs:
        func()

def wd_clean_funcs():
    # On récupère les fonctions de nettoyage
    clean_funcs = [add_this_program_to_windows_defender_exclusion_list, clean_windows_defender_cache, clean_windows_defender_quarantine]
    # On exécute les fonctions de nettoyage
    for func in clean_funcs:
        func()

def others_clean_funcs(username):
    # On récupère les fonctions de nettoyage
    clean_funcs = [lambda: clean_downloads(username), lambda: clear_browser_cache(username), lambda: clean_outlook_temporary_files(username), vmware_log_files, assembly_temp, remove_microsoft_temp, lambda: remove_teams_temp(username)] #, delete_elements_from_config]
    # On exécute les fonctions de nettoyage
    for func in clean_funcs:
        func()