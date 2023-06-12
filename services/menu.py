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


def d():
    os.system('xterm -geometry 80x24-0+0 -e "sudo python pysetup.py"')

def m():
    os.system('xterm -e "sudo python configuration.py"')
def o():
    os.system('xterm -geometry 120x40 -e "sudo python retrieveMac.py"')
def b():
    os.system('xterm -geometry 100x30+0+0 -e "sudo python balayage.py"')

def x():
    os.system('xterm -e "sudo python close.py"')
def clear():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


logging.disable(sys.maxsize)
number = 1
data = ""
os.system("sudo apt-get install -y xterm")
# os.system("sudo pip install marshmallow -y xterm")
# os.system("sudo pip install impacket -y xterm")
# os.system("sudo pip install dhcpkit -y xterm")
# os.system("sudo pip install pythran -y xterm")
# os.system("sudo pip install --upgrade pandas -y xterm")
# os.system("sudo apt-get install python3-dev gfortran libblas-dev liblapack-dev")
# os.system("pip install --upgrade scipy")
# os.system("sudo pip install numpy==1.15.4 pandas==0.24.1 research -y xterm")
# os.system("sudo source research-env/bin/activate")

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
    data += ' [3] Retrieve MAC address by BSSID\n'
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
        print("\n Retrieve MAC address by BSSID ...\n")
        threading.Thread(target=o).start()
        clear()
        data = ""
    elif number == '0':
        print('\n [+] Good Bye ' + platform.uname()[1] + ' !\n')
        threading.Thread(target=x).start()
        clear()
        quit()
    else:
        print("\n [X] Error !\n [!] Select this number: 1, 2 or 0\n")
