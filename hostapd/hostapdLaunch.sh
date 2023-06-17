#!/bin/bash

# Installation de hostapd
apt install hostapd

# Lancement de hostapd en mode débogage
hostapd -dd -K "$hostapd_directory/hostapd.conf"

read -p "Appuyez sur Entrée pour continuer..."