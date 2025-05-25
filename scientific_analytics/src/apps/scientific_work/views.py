from .serialisers import ScientificWorkSerializer
from .models import ScientificWork
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .utils.upload_file import handle_uploaded_file

class ScientyficWorkListView(viewsets.ModelViewSet):
    queryset = ScientificWork.objects.all()
    serializer_class = ScientificWorkSerializer
    
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_files(request):
    files = request.FILES.getlist('files')  

    for f in files:
        handle_uploaded_file(f)  

    return Response({'message': 'Файлы получены'})

