import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema.settings')

import django
django.setup()

from django.contrib.auth.models import User

# Remove usuários existentes
User.objects.all().delete()

# Cria novo superusuário
User.objects.create_superuser(
    username='admin',
    email='admin@exemplo.com',
    password='sicredi2024'
)

print('Superusuário criado com sucesso!') 