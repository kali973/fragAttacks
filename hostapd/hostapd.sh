#!/bin/bash

# Copier defconfig vers .config
cp defconfig .config

# Nettoyer le répertoire
make clean

# Compiler le projet avec 4 threads
make -j 4
