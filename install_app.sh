#!/bin/bash

sudo apt update
sudo apt install python3-pip

pip3 install --upgrade pip
pip install -r requirements.txt
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install -U sentence-transformers

# pip3 install --upgrade pip
# pip3 install numpy pandas

# pip3 install -U numpy scikit-learn

# pip install contractions
# pip install -U sentence-transformers


