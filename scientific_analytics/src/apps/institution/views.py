from rest_framework import generics
from .models import Institution
from .serialisers import InstitutionSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets

class InstitutionListView(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer

class InstitutionListCreateView(generics.ListCreateAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class InstitutionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
