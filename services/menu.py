import logging
import os
import platform
import sys
import threading


def a():
    os.system("wireshark")


def b():
    os.system('xterm -geometry 80x24+0+0 -e "sudo python build.py"')


def d():
    os.system('xterm -geometry 80x24-0+0 -e "sudo python pysetup.py"')


def c():
    os.system("xterm -e \"sudo python scan.py\"")


def clear():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


logging.disable(sys.maxsize)
number = 1
data = ""
os.system("sudo apt-get install -y xterm")
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
    data += ' [1] Configuration de l"environnement\n'
    data += ' [2] Scan réseau\n'
    data += ' [0] Exit\n'
    print(data)
    number = input(" Number~# ")
    if number == '1':
        print("\n Configuration de l'environnement...\n")
        threading.Thread(target=b).start()
        s = threading.Timer(10, d)
        s.start()
        print("\033[H\033[J", end="")
        data = ""
    elif number == '2':
        print("\n Scan réseau ...\n")
        threading.Thread(target=c).start()
        clear()
        data = ""
    elif number == '0':
        print('\n [+] Good Bye ' + platform.uname()[1] + ' !\n')
        command = ['sudo', 'service', 'NetworkManager', 'start']
        subprocess.run(command)
        quit()
    else:
        print("\n [X] Error !\n [!] Select this number: 1, 2 or 0\n")
