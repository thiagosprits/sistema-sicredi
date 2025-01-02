#!/usr/bin/env bash
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'sicredi2024') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell 