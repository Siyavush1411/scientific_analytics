from .serialisers import ScientificWorkSerializer
from .models import ScientificWork
from rest_framework import viewsets

class ScientyficWorkListView(viewsets.ModelViewSet):
    queryset = ScientificWork.objects.all()
    serializer_class = ScientificWorkSerializer