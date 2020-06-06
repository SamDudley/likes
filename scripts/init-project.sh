# Setup backend.
cd backend

virtualenv --python=python3 venv

. venv/bin/activate

pip install -r requirements.txt

deactivate

# Setup frontend.
cd ../frontend

npm install
