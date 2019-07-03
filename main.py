# -*- coding: utf-8 -*-
# Importation des bibliothèques nécessaires
from tkinter import *
from tkinter import filedialog
from library.main_window import *

# Création du dictionnaire qui stock les objets file
savedFile = {1:""}

# Création d'une instance sur la classe principale

root = BlockNote_window("root","content","icons_menu")

root.create_window() 
root.add_icons_menu()
root.add_text() 
root.add_icons() 
root.add_menu() 
root.generate()



