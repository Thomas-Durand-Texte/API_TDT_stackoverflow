#!/bin/bash

# sudo apt update
# sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools python3-venv

python3 -m venv .APIenv
source .APIenv/bin/activate

pip install wheel

pip install --upgrade pip

# pip install gunicorn flask

pip install -r requirements.txt
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install -U sentence-transformers

deactivate

# pip3 install --upgrade pip
# pip3 install numpy pandas

# pip3 install -U numpy scikit-learn

# pip install contractions
# pip install -U sentence-transformers


