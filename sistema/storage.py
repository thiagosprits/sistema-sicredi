import os
from google.cloud import storage

def download_db():
    """Download database from Cloud Storage"""
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket('sistema-sicredi')
        blob = bucket.blob('db.sqlite3')
        blob.download_to_filename('/tmp/db.sqlite3')
    except Exception:
        # Se não existir, cria um novo
        pass

def upload_db():
    """Upload database to Cloud Storage"""
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket('sistema-sicredi')
        blob = bucket.blob('db.sqlite3')
        blob.upload_from_filename('/tmp/db.sqlite3')
    except Exception as e:
        print(f"Error uploading DB: {e}") 