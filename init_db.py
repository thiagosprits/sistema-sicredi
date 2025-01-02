import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema.settings')

import django
django.setup()

from django.contrib.auth.models import User
from django.core.management import call_command

def init_db():
    # Executa as migrações
    call_command('migrate', '--noinput')
    
    # Cria o superusuário se não existir
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'sicredi2024')

if __name__ == '__main__':
    init_db() 