#!/bin/sh

pip install requirements
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
