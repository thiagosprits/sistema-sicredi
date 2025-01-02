from pymongo import MongoClient
from django.conf import settings

def get_db():
    client = MongoClient(settings.MONGODB_URI)
    return client.sicredi

def save_user(username, password, email):
    db = get_db()
    users = db.users
    user_data = {
        'username': username,
        'password': password,
        'email': email,
        'is_active': True,
        'is_staff': True,
        'is_superuser': True
    }
    return users.insert_one(user_data) 