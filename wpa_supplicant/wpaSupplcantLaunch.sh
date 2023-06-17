#!/bin/bash

# Exécution de wpa_supplicant en mode débogage
wpa_supplicant -D nl80211 -i wlan1 -c client.conf -dd -K

read -p "Appuyez sur Entrée pour continuer..."

