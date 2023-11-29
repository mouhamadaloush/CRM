#!/bin/bash

#building the project

python3.9 -m pip install -r requirements.txt

pyhton3.9 manage.py makemigrations --noinput
pyhton3.9 manage.py migrate --noinput
pyhton3.9 manage.py collectstatic --noinput --clear
