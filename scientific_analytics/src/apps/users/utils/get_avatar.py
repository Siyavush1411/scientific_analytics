import os
from django.conf import settings

def handle_uploaded_avatar(f):
    path = os.path.join('avatar/', f.name)
    