import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema.settings')

import django
django.setup()

from django.contrib.auth.models import User

# Cria um superusuário
username = 'admin'
email = 'admin@example.com'
password = 'sicredi2024'

try:
    user = User.objects.create_superuser(username=username, email=email, password=password)
    print(f'Usuário {username} criado com sucesso!')
except Exception as e:
    print(f'Erro ao criar usuário: {e}') 