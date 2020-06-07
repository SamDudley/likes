#!/bin/bash

cd backend

. venv/bin/activate

python manage.py test

deactivate
