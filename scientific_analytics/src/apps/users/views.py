from .serialisers import UserListSerializer, UserTokenObtainPairSerializer, UserProfileSerializer
from .models import User
from rest_framework import viewsets
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .utils.get_avatar import handle_uploaded_avatar
from django.conf import settings


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
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_avatar(request):
    files = request.FILES.getlist('files')  

    for f in files:
        handle_uploaded_avatar(f)  

    return Response({'message': 'Файлы получены'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_current_user(request):
    return Response({
        'id': request.user.id,
        'username': request.user.username,
        'email': request.user.email
    })
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_avatar(request):
    profile = request.user.profile  # через OneToOne
    serializer = AvatarSerializer(profile)
    return Response(serializer.data)
