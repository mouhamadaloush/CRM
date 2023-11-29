#!/bin/bash

#building the project

python3 -m pip install -r requirements.txt

pyhton3 manage.py makemigrations --noinput
pyhton3 manage.py migrate --noinput
pyhton3 manage.py collectstatic --noinput --clear
