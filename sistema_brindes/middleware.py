import os
from django.db import connection
from django.core.management import call_command
from django.contrib.auth.models import User
from sistema.storage import download_db, upload_db

class DatabaseInitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.initialized = False

    def __call__(self, request):
        if not self.initialized:
            download_db()
            with connection.cursor() as cursor:
                try:
                    cursor.execute("SELECT * FROM auth_user LIMIT 1")
                except:
                    call_command('migrate', '--noinput')
                    if not User.objects.filter(username='admin').exists():
                        User.objects.create_superuser('admin', 'admin@example.com', 'sicredi2024')
            upload_db()
            self.initialized = True
        
        response = self.get_response(request)
        upload_db()  # Upload after each request
        return response 