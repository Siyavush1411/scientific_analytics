from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
        'id',
        'username',
        'first_name',
        'last_name',
        'patronymic',
        'rating',
        'status',
        ]
        
    def get_status_field_user(self):
        from apps.status.models import Status
        return Status.objects.get()
        
    def create(self, data):
        data['status'] = self.get_status_field_user()
        return User.objects.create_user(**data)

class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token