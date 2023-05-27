#!/bin/bash

source .APIenv/bin/activate

# python3 app.py
gunicorn --bind 0.0.0.0:5000 wsgi:app

deactivate

echo "vitual env deactivated"
