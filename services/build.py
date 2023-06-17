import os
import subprocess

# Mettre à jour les paquets disponibles
os.system("sudo apt-get update")

# Installer les dépendances requises
os.system("sudo apt-get install libnl-3-dev libnl-genl-3-dev libnl-route-3-dev libssl-dev \
    libdbus-1-dev git pkg-config build-essential macchanger net-tools python3-venv \
    aircrack-ng rfkill")

n = 1  # Nombre de niveaux à remonter à partir du répertoire courant

current_directory = os.getcwd()
parent_directory = current_directory

# Remonter n niveaux dans l'arborescence des répertoires
for _ in range(n):
    parent_directory = os.path.dirname(parent_directory)

# Rechercher et exécuter le script build.sh dans le répertoire 'research'
for root, dirs, files in os.walk(parent_directory):
    if 'research' in dirs:
        research_dir = os.path.join(root, 'research')
        build_sh_path = os.path.join(research_dir, 'build.sh')
        if os.path.isfile(build_sh_path):
            print(f"Exécution de build.sh dans {research_dir}")
            os.chdir(research_dir)
            os.system('chmod +x build.sh')  # Changer les permissions pour le rendre exécutable
            subprocess.run(['bash', 'build.sh'], cwd=research_dir, check=True, stderr=subprocess.DEVNULL)
            break  # Sortir de la boucle après avoir exécuté build.sh

# Installer les dépendances requises
os.system("apt-get install libnl-genl-3-dev")
os.system("apt-get install libdbus-1-dev")
os.system("apt-get install libssl-dev")

# Rechercher et exécuter le script wpaSupplicant.sh dans le répertoire 'wpa_supplicant'
for root, dirs, files in os.walk(parent_directory):
    if 'wpa_supplicant' in dirs:
        research_dir = os.path.join(root, 'wpa_supplicant')
        build_sh_path = os.path.join(research_dir, 'wpaSupplicant.sh')
        if os.path.isfile(build_sh_path):
            print(f"Exécution de wpaSupplicant.sh dans {research_dir}")
            os.chdir(research_dir)
            os.system('chmod +x wpaSupplicant.sh')  # Changer les permissions pour le rendre exécutable
            subprocess.run(['bash', 'wpaSupplicant.sh'], cwd=research_dir, check=True, stderr=subprocess.DEVNULL)
            break  # Sortir de la boucle après avoir exécuté wpaSupplicant.sh

# Rechercher et exécuter le script hostapd.sh dans le répertoire 'hostapd'
for root, dirs, files in os.walk(parent_directory):
    if 'hostapd' in dirs:
        research_dir = os.path.join(root, 'hostapd')
        build_sh_path = os.path.join(research_dir, 'hostapd.sh')
        if os.path.isfile(build_sh_path):
            print(f"Exécution de hostapd.sh dans {research_dir}")
            os.chdir(research_dir)
            os.system('chmod +x hostapd.sh')  # Changer les permissions pour le rendre exécutable
            subprocess.run(['bash', 'hostapd.sh'], cwd=research_dir, check=True, stderr=subprocess.DEVNULL)
            break  # Sortir de la boucle après avoir exécuté hostapd.sh

print()
input("Appuyez sur Entrée pour continuer...")
