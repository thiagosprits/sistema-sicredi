from firebase_admin import credentials, initialize_app, firestore
import os

# Inicializa o Firebase Admin
cred = credentials.ApplicationDefault()
initialize_app(cred)

# Obtém uma referência do Firestore
db = firestore.client()

class FirestoreBackend:
    def __init__(self):
        self.db = db
        self.users = self.db.collection('users')

    def authenticate(self, request, username=None, password=None):
        user_doc = self.users.where('username', '==', username).get()
        if not user_doc:
            return None
        user = user_doc[0].to_dict()
        if user['password'] == password:  # Na prática, use hash
            return user
        return None

    def get_user(self, user_id):
        user_doc = self.users.document(user_id).get()
        if user_doc.exists:
            return user_doc.to_dict()
        return None 