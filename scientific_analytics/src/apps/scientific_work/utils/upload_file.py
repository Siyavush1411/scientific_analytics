import os
from django.conf import settings

def handle_uploaded_file(f):
    path = os.path.join(settings.MEDIA_ROOT, f.name)
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
