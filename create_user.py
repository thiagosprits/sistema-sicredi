#!/usr/bin/env python
import os
import django
import sys

def create_superuser():
    from django.contrib.auth.models import User
    
    try:
        # Remove usuários existentes
        User.objects.all().delete()
        
        # Cria novo superusuário
        User.objects.create_superuser(
            username='admin',
            email='admin@exemplo.com',
            password='sicredi2024'
        )
        print('Superusuário criado com sucesso!')
    except Exception as e:
        print(f'Erro ao criar superusuário: {e}')

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema.settings')
    django.setup()
    create_superuser() 