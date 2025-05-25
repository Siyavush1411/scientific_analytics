from django.db import connections
from ..models import User
from transliterate import translit
from apps.scientific_work.models import ScientificWork
from django.db import IntegrityError

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
        cursor.execute('SELECT * FROM _author')
        authors = dictfetchall(cursor)

    for record in authors:
        try:
            User.objects.update_or_create(material_user_id=record['id'], defaults={
                'first_name': record['name'].split()[0],
                'last_name': record['name'].split()[1]  if len(record['name'].split()) > 1 else record['name'],
                'username':translit(record['name'], 'ru', reversed=True),
                'degree':record['degree'],
                'material_user_id':record['id'],
            }
            )
        except IntegrityError:
            print(f"⛔ Уже есть: {record['name']} — пропущено")
            continue


def synch_scientific_works():
    with connections['secondary'].cursor() as cursor:
        cursor.execute('SELECT * FROM _material')
        works = dictfetchall(cursor)

    for record in works:
        try:
            obj, created = ScientificWork.objects.update_or_create(
                material_work_id=record['id'],
                defaults={
                    'work_name': record['name'],
                    'date_of_publish': record['date_publish'],
                    'conferenc_name': record['conference_name'],
                    'file_path': record['file_path'],
                    'category_id': record['material_direction_id'],
                    'work_rating': 0,
                    'uniquenes_score': 0,
                }
            )

            authors = User.objects.filter(material_user_id=record['user_id'])
            obj.author.set(authors)
            
            obj.save()
            print(f"✅ {'Создан' if created else 'Обновлён'}: {record['name']}")
        except IntegrityError as e:
            print(f"⛔ Уже есть: {record['name']} — пропущено {e}")
            continue
        
@api_view(['POST'])
@permission_classes([IsAdminUser])
def sync_authors(request):
    synch_scientific_works()
    return Response({'detail': 'ok'}, status=status.HTTP_200_OK)