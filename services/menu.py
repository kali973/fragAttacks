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
    os.system('xterm -geometry 80x24+0+0 -e "sudo python monitoringAccess.py"')


def d():
    os.system('xterm -geometry 80x24-0+0 -e "sudo python pysetup.py"')


def m():
    os.system('xterm -e "sudo python configuration.py"')


def o():
    os.system('xterm -geometry 120x30-0+0 -e "sudo python retrieveMac.py"')


def b():
    os.system('xterm -geometry 100x30+0+0 -e "sudo python balayage.py"')
def v():
    os.system('xterm -e "sudo python modprobe.py"')
def k():
    os.system('xterm -geometry 100x30+0+0 -e "sudo python CapturePaquet.py"')
def q():
    os.system('xterm -geometry 100x30+0+0 -e "sudo python 4WayHanddshake.py"')

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
    data += ' [D] Monitoring of access point\n'
    data += ' [4] Capture des paquets du BSSID\n'
    data += ' [5] 4 Way handshake\n'
    data += ' [6] Attaque Brute force\n'
    data += ' [7] Create 4 virtual interface Wifi\n'
    data += ' [8] Starting hostapd (Virtual AP on wlan4) and wpa_supplicant (Client connection on wlan4)\n'
    data += ' [9] Test de vulnerability\n'
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
        print("\n Scan network ( faire Ctrl C for stop scanning network) ...\n")
        b_thread = threading.Thread(target=b)
        b_thread.start()  # Start the first thread
        b_thread.join()  # Wait for the first thread to finish before proceeding

        o_thread = threading.Thread(target=o)
        o_thread.start()  # Start the second thread
        clear()
        data = ""
    elif number == '3':
        print("\n Select target by BSSID ...\n")
        threading.Thread(target=o).start()
        clear()
        data = ""
    elif number == 'D':
        print("\n Monitoring of access point ...\n")
        threading.Thread(target=l).start()
        clear()
        data = ""
    elif number == '4':
        print("\n Capture des paquets du BSSID ...\n")
        threading.Thread(target=k).start()
        clear()
        data = ""
    elif number == '5':
        print("\n 4 Way handshake ...\n")
        threading.Thread(target=q).start()
        clear()
        data = ""
    elif number == '6':
        print("\n Attaque brute force ...\n")
        threading.Thread(target=w).start()
        clear()
        data = ""
    elif number == '7':
        print("\n Create 4 virtual interface Wifi  ...\n")
        s = threading.Timer(5, v)
        s.start()
        clear()
        data = ""
    elif number == '8':
        print("\n Starting hostapd (Virtual AP on wlan4) and wpa_supplicant (Client connection on wlan4) ...\n")
        threading.Thread(target=h).start()
        s = threading.Timer(30, i)
        s.start()
        clear()
        data = ""
    elif number == '9':
        print("\n Test de vulnerability ...\n")
        # threading.Thread(target=s).start()
        # s = threading.Timer(10, i)
        # s.start()
        clear()
        data = ""
    elif number == '0':
        print('\n [+] Good Bye ' + platform.uname()[1] + ' !\n')
        threading.Thread(target=x).start()
        clear()
        quit()
    else:
        print("\n [X] Error !\n [!] Select this number: 1, 2 or 0\n")
