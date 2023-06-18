import os

# Lance la commande modprobe
os.system("modprobe mac80211_hwsim radios=4")

# Exécute la commande iwconfig
os.system("iwconfig")

print()
input("Appuyez sur Entrée pour continuer...")