import os
import subprocess

n = 1  # Nombre de niveaux à remonter à partir du répertoire courant

current_directory = os.getcwd()
parent_directory = current_directory

for _ in range(n):
    parent_directory = os.path.dirname(parent_directory)

for root, dirs, files in os.walk(parent_directory):
    if 'services' in dirs:
        research_dir = os.path.join(root, 'services')
        menu_py_path = os.path.join(research_dir, 'menu.py')
        if os.path.isfile(menu_py_path):
            print(f"Exécution de menu.py dans {research_dir}")
            os.chdir(research_dir)
            os.system('chmod +x menu.py')  # Changer les permissions pour le rendre exécutable
            subprocess.run(['python', 'menu.py'], cwd=research_dir, check=True, stderr=subprocess.DEVNULL)
            break  # Sortir de la boucle après avoir exécuté menu.py
