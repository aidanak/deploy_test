#!/usr/bin/env bash
source '../envs/deploy_test/bin/activate'
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate --noinput