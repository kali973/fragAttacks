import subprocess

def is_wifi_connected():
    try:
        output = subprocess.check_output(['iw', 'dev']).decode('utf-8')
        if 'wlan0' in output:  # Remplacez 'wlan0' par l'interface WiFi correspondante
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False

def run_command(command):
    try:
        output = subprocess.check_output(command, shell=True).decode('utf-8')
        print(f"\033[1;31m{command}\033[0m")  # Affichage de la commande en caractères gras et rouges
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de la commande : {e}")

if is_wifi_connected():
    print("Le dongle WiFi est connecté.")
    print("Liste des périphériques USB :")
    run_command('lsusb')
    print("\nInformations détaillées du dongle WiFi :")
    run_command('lsusb -vs 001:002')
    print("\nInformations du dongle WiFi :")
    run_command('ethtool -i wlan0')  # Remplacez 'wlan0' par l'interface WiFi correspondante

    # Désactiver la carte WiFi
    run_command('sudo ip link set wlan0 down')

    # Activer le mode monitor
    run_command('sudo iwconfig wlan0 mode monitor')

    # Réactiver la carte WiFi
    run_command('sudo ip link set wlan0 up')

    print("\nInformations de la carte WiFi :")
    run_command('iwconfig wlan0')
else:
    print("Le dongle WiFi n'est pas connecté.")

print()
input("Appuyez sur Entrée pour continuer...")
