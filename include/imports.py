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
from src.windows_clean_funcs import *
from src.wd_clean_funcs import *
from src.utils import *

def windows_clean_funcs():
    # On récupère les fonctions de nettoyage
    clean_funcs = [clean_thumbnails, clean_recycle_bin, clean_language_resources, clean_logs, clean_windows_update_delivery_optimization]
    # On exécute les fonctions de nettoyage
    for func in clean_funcs:
        func()

def utils():
    # On récupère les fonctions de nettoyage
    clean_funcs = [set_console_title, check_if_program_is_started_with_admin_rights, check_if_win10_or_higher, show_confirmation_dialog, show_error_dialog]
    # On exécute les fonctions de nettoyage
    for func in clean_funcs:
        func()
