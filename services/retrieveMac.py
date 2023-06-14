import csv
import os
import subprocess
import tkinter as tk
from tinydb import TinyDB

def afficher_selection():
    # Création d'une nouvelle fenêtre pour afficher la sélection
    selection_window = tk.Tk()
    selection_window.title("Sélection")

    # Création d'un widget Label pour afficher le titre de la sélection
    selection_label = tk.Label(selection_window, text="Élément sélectionné :")
    selection_label.pack()

    # Récupération des données de la base de données de sélection
    selection_db = TinyDB('selection.json')
    selection_table = selection_db.table('_default')
    selection_data = selection_table.all()

    # Affichage de la sélection dans un widget Label formaté
    header_label = tk.Label(selection_window, text="Num. Seq.    BSSID                NetType    ESSID                          Channel  Encryption")
    header_label.pack()

    for i, item in enumerate(selection_data, start=1):
        item_label = tk.Label(selection_window, text="{:<12d} {:<20s} {:<10s} {:<30s} {:<8s} {:<12s}".format(i, item['BSSID'], item['NetType'], item['ESSID'], item['Channel'], item['Encryption']))
        item_label.pack()

    # Fermeture de la base de données de sélection
    selection_db.close()

    # Démarrage de la boucle principale de la fenêtre de sélection
    selection_window.mainloop()


# Vérification de l'existence du fichier "database.json"
db_file = 'database.json'

if not os.path.exists(db_file):
    print(f"Le fichier '{db_file}' n'existe pas. Veuillez exécuter l'étape précédente pour créer la base de données.")
    exit()

# Lecture du fichier CSV
with open('out-01.csv-01.kismet.csv', 'r') as file:
    reader = csv.DictReader(file, delimiter=';')
    data = list(reader)


# Affichage des données en colonnes
print("{:<12s} {:<20s} {:<10s} {:<30s} {:<8s} {:<12s}".format("Num. Seq.", "BSSID", "NetType", "ESSID", "Channel", "Encryption"))
print(" ")
for i, item in enumerate(data, start=1):
    print("{:<12d} {:<20s} {:<10s} {:<30s} {:<8s} {:<12s}".format(i, item['BSSID'], item['NetType'], item['ESSID'], item['Channel'], item['Encryption']))

print(" ")
# Demande de saisie du numéro de séquence
sequence_input = input("Veuillez saisir un numéro de séquence : ")

# Vérification de l'entrée utilisateur
selected_item = None
for i, item in enumerate(data, start=1):
    if str(i) == sequence_input:
        selected_item = item
        break

# Si aucun élément correspondant n'est trouvé, afficher un message d'erreur
if selected_item is None:
    print("Aucune donnée correspondante pour le numéro de séquence saisi.")
    exit()

# Création de la base de données pour la sélection
selection_db = TinyDB('selection.json')
selection_table = selection_db.table('_default')

# Suppression des anciennes données de sélection
selection_table.truncate()

# Insertion de l'élément sélectionné dans la base de données de sélection
selection_table.insert(selected_item)

# Fermeture de la base de données de sélection
selection_db.close()

# Affichage de la sélection dans une fenêtre séparée
afficher_selection()
