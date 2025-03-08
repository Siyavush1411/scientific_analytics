from .serialisers import ScientificWorkSerializer
from .models import User
from rest_framework import viewsets

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ScientificWorkSerializer