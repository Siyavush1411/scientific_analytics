from django.db import connections
from ..models import User
from transliterate import translit
from apps.scientific_work.models import ScientificWork

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status

def dictfetchall(cursor):
    """Получает результат запроса в виде списка словарей"""
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def synch():
    with connections['secondary'].cursor() as cursor:
        cursor.execute('SELECT * FROM author')
        authors = dictfetchall(cursor)

    for record in authors:
        User.objects.create(
            username=translit(record['name'], 'ru', reversed=True),
            degree=record['degree'],
            material_user_id=record['id']
        )
        
        
@api_view(['POST'])
@permission_classes([IsAdminUser])
def sync_authors(request):
    synch()
    return Response({'detail': 'ok'}, status=status.HTTP_200_OK)