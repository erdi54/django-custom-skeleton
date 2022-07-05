#!/bin/bash

echo "Pulling New Version From Git Origin..."
git pull origin main
echo "Activating Virtual environment..."
source venv/bin/activate
echo "Installing Dependencies..."
pip install -r requirements.txt
echo "Migrating Database..."
python manage.py migrate
echo "Collecting static files..."
python manage.py collectstatic --no-input
echo "Restarting gunicorn..."
sudo service gunicorn restart
sleep 10
echo "Restarting Celery..."
sudo service celery restart
echo "Restarting CeleryBeat..."
sudo service celerybeat restart
echo "Finished!"
