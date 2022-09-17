#!/bin/bash

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Start server
echo "Starting server"
gunicorn bakeoff_python_django.wsgi:application --bind 0.0.0.0:$PORT --workers=3