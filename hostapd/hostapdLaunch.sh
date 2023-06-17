#!/bin/bash

# Se déplacer dans le répertoire fragAttacks
cd /root/PycharmProjects/fragAttacks/hostapd/ || exit 1

# Recherche du fichier hostapd.conf
hostapd_file=$(find . -name "hostapd.conf" 2>/dev/null)

if [ -z "$hostapd_file" ]; then
  echo "Le fichier hostapd.conf n'a pas été trouvé."
  exit 1
fi

# Lancement de la commande hostapd
hostapd -dd -K "$hostapd_file"



read -p "Appuyez sur Entrée pour continuer..."
