#!/bin/bash

# Copie du fichier defconfig vers .config
cp defconfig .config

# Nettoyage du répertoire
make clean

# Compilation avec 4 threads
make -j 4
