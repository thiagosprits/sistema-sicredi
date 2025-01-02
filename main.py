import os
from sistema.wsgi import application

# Configurar o ambiente
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema.settings')

# Importar Django e configurar
import django
django.setup()

# Criar as tabelas
from django.core.management import call_command
call_command('migrate')

# Criar superusuário
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'sicredi2024')

app = application 