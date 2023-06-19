import os
import subprocess


def lancer_aircrack_ng(nom_fichier_cap, nom_fichier_wordlist):
    command_aircrack = ['aircrack-ng', nom_fichier_cap, '-w', nom_fichier_wordlist]
    subprocess.call(command_aircrack)


# Fichier .cap à utiliser
nom_fichier_cap = '4way-01.cap'

# Fichier wordlist à utiliser
nom_fichier_wordlist = 'rockyou.txt'

n = 1  # Nombre de niveaux à remonter à partir du répertoire courant

current_directory = os.getcwd()
parent_directory = current_directory

# Remonter n niveaux dans l'arborescence des répertoires
for _ in range(n):
    parent_directory = os.path.dirname(parent_directory)

# Rechercher et exécuter le script build.sh dans le répertoire 'research'
for root, dirs, files in os.walk(parent_directory):
    if 'dictionnary' in dirs:
        research_dir = os.path.join(root, 'dictionnary')
        nom_fichier_wordlist = os.path.join(research_dir, 'rockyou.txt')
        if os.path.isfile(nom_fichier_wordlist):
            os.chdir(research_dir)
            break  # Sortir de la boucle après avoir exécuté build.sh

n = 1  # Nombre de niveaux à remonter à partir du répertoire courant

current_directory = os.getcwd()
parent_directory = current_directory

# Remonter n niveaux dans l'arborescence des répertoires
for _ in range(n):
    parent_directory = os.path.dirname(parent_directory)

# Rechercher et exécuter le script build.sh dans le répertoire 'research'
for root, dirs, files in os.walk(parent_directory):
    if 'services' in dirs:
        way_dir = os.path.join(root, 'services')
        nom_fichier_cap = os.path.join(way_dir, '4way-01.cap')
        if os.path.isfile(nom_fichier_cap):
            os.chdir(way_dir)
            break
# Appel de la fonction pour lancer aircrack-ng
lancer_aircrack_ng(nom_fichier_cap, nom_fichier_wordlist)

print()
input("Appuyez sur Entrée pour continuer...")
