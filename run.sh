#!/bin/sh

python3 manage.py migrate
# number of workers = (2 x $num_cores) + 1
gunicorn factcoin.wsgi:application -b 0.0.0.0:8000 -w 2 --preload --log-level=INFO
