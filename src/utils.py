from include.imports import ctypes, os, platform, sys, messagebox

def set_console_title():
    ctypes.windll.kernel32.SetConsoleTitleW("SweePy v0.3-beta")

def check_if_program_is_started_with_admin_rights():
    try:
        # Vérifier si le programme est lancé en tant qu'administrateur
        is_admin = os.getuid() == 0
        if is_admin:
            return True
        else:
            messagebox.showerror("Erreur", "Ce programme doit être lancé en tant qu'administrateur")
    except:
        return False

def check_if_win10_or_higher():
    if platform.release() == "10" or platform.release() == "11":
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