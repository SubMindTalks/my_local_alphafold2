#!/bin/bash
set -e

echo "Step 1: Update and upgrade system packages"
sudo apt-get update -y
sudo apt-get upgrade -y

echo "Step 2: Install essential dependencies"
sudo apt-get install -y \
    build-essential \
    cmake \
    git \
    wget \
    curl \
    aria2 \
    python3 \
    python3-pip \
    python3-venv \
    software-properties-common \
    tree

echo "Step 3: Install CUDA Toolkit 12.6"
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-ubuntu2404.pin
sudo mv cuda-ubuntu2404.pin /etc/apt/preferences.d/cuda-repository-pin-600
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/3bf863cc.pub
sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/ /"
sudo apt-get update -y
sudo apt-get install -y cuda-toolkit-12-6
export PATH=/usr/local/cuda-12.6/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-12.6/lib64:$LD_LIBRARY_PATH
echo 'export PATH=/usr/local/cuda-12.6/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-12.6/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc

echo "Step 4: Download and install Anaconda"
wget https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh
bash Anaconda3-2024.10-1-Linux-x86_64.sh -b -p ~/anaconda3
export PATH=~/anaconda3/bin:$PATH
echo 'export PATH=~/anaconda3/bin:$PATH' >> ~/.bashrc
source ~/.bashrc

echo "Preparation complete!"
