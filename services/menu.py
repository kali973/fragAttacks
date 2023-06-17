import logging
import os
import platform
import subprocess
import sys
import threading


def a():
    os.system("wireshark")


def e():
    os.system('xterm -geometry 80x24+0+0 -e "sudo python build.py"')


def w():
    os.system('xterm -geometry 80x24+0+0 -e "sudo python AttaqueBruteForce.py"')


def l():
    os.system('xterm -geometry 80x24+0+0 -e "sudo python 4WayHandshake.py"')


def d():
    os.system('xterm -geometry 80x24-0+0 -e "sudo python pysetup.py"')


def m():
    os.system('xterm -e "sudo python configuration.py"')


def o():
    os.system('xterm -geometry 120x30-0+0 -e "sudo python retrieveMac.py"')


def b():
    os.system('xterm -geometry 100x30+0+0 -e "sudo python balayage.py"')
def v():
    os.system('modprobe mac80211_hwsim radios=4')
def k():
    os.system('xterm -geometry 100x30+0+0 -e "sudo python CapturePaquet.py"')


def x():
    os.system('xterm -e "sudo python close.py"')

def h():
    os.system('xterm -e "sudo python hostapd.py"')

def i():
    os.system('xterm -e "sudo python wpaSupplicant.py"')

def clear():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


logging.disable(sys.maxsize)
number = 1
data = ""
os.system("sudo apt-get install -y python3.11-venv")
os.system("sudo apt-get install -y xterm")

# Installation de tinydb sans afficher les avertissements
subprocess.run(['sudo', 'pip', 'install', 'tinydb'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

os.environ['TERM'] = 'xterm'
path = os.getcwd()

while number != '0':
    data += ' ----------------------------\n'
    if os.name == "nt":
        print(' [!] Please run the script on Linux Machine !')
        quit()
    elif os.name != "nt":
        data = (' ----------------------------\n')
        data += ' Hi ' + platform.uname()[1] + '\n'

    data += ' ----------------------------\n'
    data += ' Select option:\n'
    data += ' [1] Configuration environment\n'
    data += ' [2] Scan network (Crtl-C to stop scan)\n'
    data += ' [3] Select target by BSSID\n'
    data += ' [4] Capture des paquets du BSSID\n'
    data += ' [5] Attaque Brute force\n'
    data += ' [6] Create 4 virtual interface Wifi\n'
    data += ' [7] Starting hostapd and wpa_supplicant\n'
    data += ' [0] Exit\n'
    print(data)
    number = input(" Number~# ")
    if number == '1':
        print("\n Configuration de l'environnement...\n")
        threading.Thread(target=e).start()
        s = threading.Timer(10, d)
        s.start()
        m = threading.Timer(10, m)
        m.start()
        print("\033[H\033[J", end="")
        print("\033[H\033[J", end="")
        data = ""
    elif number == '2':
        print("\n Scan réseau ...\n")
        threading.Thread(target=b).start()
        clear()
        data = ""
    elif number == '3':
        print("\n Select target by BSSID ...\n")
        threading.Thread(target=o).start()
        clear()
        data = ""
    elif number == '4':
        print("\n Capture des paquets du BSSID ...\n")
        threading.Thread(target=k).start()
        clear()
        data = ""
    elif number == '5':
        print("\n Attaque brute force ...\n")
        threading.Thread(target=w).start()
        clear()
        data = ""
    elif number == '6':
        print("\n Create 4 virtual interface Wifi  ...\n")
        threading.Thread(target=v).start()
        clear()
        data = ""
    elif number == '7':
        print("\n Starting hostapd and wpa_supplicant ...\n")
        threading.Thread(target=h).start()
        s = threading.Timer(10, i)
        s.start()
        clear()
        data = ""
    elif number == '0':
        print('\n [+] Good Bye ' + platform.uname()[1] + ' !\n')
        threading.Thread(target=x).start()
        clear()
        quit()
    else:
        print("\n [X] Error !\n [!] Select this number: 1, 2 or 0\n")
