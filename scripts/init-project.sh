#!/bin/bash

# Setup backend.
cd backend

virtualenv --python=python3 venv

. venv/bin/activate

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

deactivate

# Setup frontend.
cd ../frontend

npm install

# Setup git hooks.
cd ..

git config core.hooksPath .githooks
