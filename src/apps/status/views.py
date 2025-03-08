from .serialisers import StatusSerializer
from .models import Status
from rest_framework import viewsets

class StatusView(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer