from .serialisers import UserListSerializer, UserTokenObtainPairSerializer
from .models import User
from rest_framework import viewsets
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [permissions.AllowAny]

class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer

class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user