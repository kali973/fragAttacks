import json
import os
import subprocess
from multiprocessing import Process

def lancer_airodump_ng(bssid):
    directory = os.getcwd()
    command_airodump = ['airodump-ng', 'wlan0', '-d', bssid]
    subprocess.call(command_airodump)

# Chemin du fichier selection.json
selection_file = 'selection.json'

# Vérification de l'existence du fichier selection.json
if not os.path.exists(selection_file):
    print(f"Le fichier '{selection_file}' n'existe pas. Veuillez exécuter l'étape précédente pour créer la sélection.")
    exit()

# Lecture du fichier selection.json
with open(selection_file, 'r') as file:
    selection_data = json.load(file)

# Récupération de bssid et channel de la sélection
bssid = selection_data['_default']['1']['BSSID']
channel = selection_data['_default']['1']['Channel']

# Lancement des commandes en parallèle
process_airodump = Process(target=lancer_airodump_ng, args=(bssid,))

# Démarrage des processus
process_airodump.start()

# Attendre que les processus se terminent
process_airodump.join()
