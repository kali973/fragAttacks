import os
import subprocess

n = 1  # Nombre de niveaux à remonter à partir du répertoire courant

current_directory = os.getcwd()
parent_directory = current_directory

# Remonter n niveaux dans l'arborescence des répertoires
for _ in range(n):
    parent_directory = os.path.dirname(parent_directory)

# Rechercher et exécuter le script build.sh dans le répertoire 'research'
for root, dirs, files in os.walk(parent_directory):
    if 'wpa_supplicant' in dirs:
        research_dir = os.path.join(root, 'wpa_supplicant')
        build_sh_path = os.path.join(research_dir, 'client.conf')
        if os.path.isfile(build_sh_path):
            os.chdir(research_dir)
            command = "wpa_supplicant -D nl80211 -i wlan4 -c client.conf -dd -K"
            subprocess.run(command, shell=True, check=True)
            break

print()
input("Appuyez sur Entrée pour continuer...")