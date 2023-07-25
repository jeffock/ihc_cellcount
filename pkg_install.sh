#!/bin/bash


# Windows systems with pip

# List of packages to install
packages=(
    Pillow
)

# Create a requirements.txt file with the list of packages
echo "${packages[@]}" > requirements.txt

# Install packages using pip
pip install -r requirements.txt

# Clean up the requirements.txt file (optional)
rm requirements.txt

echo "All packages have been installed."

# 'bash auto_import.sh' in your terminal (for gitbash)


# UNIX based systems (Linux distros, macOS)

#!/bin/bash

# List of packages to download
#packages=(
#    package1
#    package2
#    package3
    # Add more package names as needed
#)

# Function to check if a package is already installed
#function is_package_installed {
#    dpkg -l "$1" | grep -q '^ii' 2>/dev/null
#}

# Update package lists
#sudo apt-get update

# Install packages
#for package in "${packages[@]}"; do
#    if ! is_package_installed "$package"; then
#        echo "Installing $package..."
#        sudo apt-get install -y "$package"
#    else
#        echo "$package is already installed."
#    fi
#done

#echo "All packages have been installed."


# 'chmod +x auto_import.sh' for Ubunto, for example (each particular os will be different)
