#!/bin/bash

# Script: requirement.sh
# Purpose: Install required Python packages and setup Termux storage

echo "Updating package list..."
pkg update -y && pkg upgrade -y

echo "Installing Python and pip..."
pkg install python -y

echo "Installing required Python packages..."
pip install --upgrade pip
pip install termcolor requests

echo "Setting up Termux storage access..."
termux-setup-storage

echo "All requirements installed successfully!"
echo "Storage linked to: $HOME/storage"