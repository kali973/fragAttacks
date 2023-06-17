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
    if 'hostapd' in dirs:
        research_dir = os.path.join(root, 'hostapd')
        build_sh_path = os.path.join(research_dir, 'hostapdLaunch.sh')
        if os.path.isfile(build_sh_path):
            os.chdir(research_dir)
            os.system('chmod +x hostapdLaunch.sh')  # Changer les permissions pour le rendre exécutable
            subprocess.run(['bash', 'hostapdLaunch.sh'], cwd=research_dir, check=True, stderr=subprocess.DEVNULL)
            break  # Sortir de la boucle après avoir exécuté hostapdLaunch.sh

