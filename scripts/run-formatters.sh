#!/bin/bash

cd backend

. venv/bin/activate

black likes

deactivate

cd ../frontend

npm run prettier:write
