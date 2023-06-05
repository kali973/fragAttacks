import os
import subprocess

n = 1  # Nombre de niveaux à remonter à partir du répertoire courant

current_directory = os.getcwd()
parent_directory = current_directory

for _ in range(n):
    parent_directory = os.path.dirname(parent_directory)

for root, dirs, files in os.walk(parent_directory):
    if 'research' in dirs:
        research_dir = os.path.join(root, 'research')
        build_sh_path = os.path.join(research_dir, 'pysetup.sh')
        if os.path.isfile(build_sh_path):
            print(f"Exécution de pysetup.sh dans {research_dir}")
            os.chdir(research_dir)
            os.system('chmod +x pysetup.sh')  # Changer les permissions pour le rendre exécutable
            subprocess.run(['bash', 'pysetup.sh'], cwd=research_dir, check=True, stderr=subprocess.DEVNULL)
            break  # Sortir de la boucle après avoir exécuté build.sh
print()
input("Press Enter to continue...")