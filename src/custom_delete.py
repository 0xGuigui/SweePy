##
##  custom_delete.py
##  SweePy
##

import os
import shutil
import sys
import ctypes
import configparser


def delete_elements_from_config(file_path):
    # Vérifier si le fichier existe
    if not os.path.isfile(file_path):
        print(f"Le fichier {file_path} n'existe pas.")
        return

    # Créer une instance de ConfigParser
    config = configparser.ConfigParser()

    # Lire le fichier de configuration
    config.read(file_path)

    # Parcourir toutes les sections
    for section in config.sections():
        # Parcourir tous les éléments de la section
        for key, value in config.items(section):
            # Remplacer %USER% par le nom de l'utilisateur actuel
            value = os.path.expanduser(value.replace('%USER%', '~'))

            # Si la clé est 'F', alors supprimer le fichier
            if key.upper() == 'F':
                if os.path.isfile(value):
                    os.remove(value)
            # Si la clé est 'P', alors supprimer le dossier
            elif key.upper() == 'P':
                if os.path.isdir(value):
                    shutil.rmtree(value)