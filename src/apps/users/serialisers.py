from rest_framework import serializers
from .models import Status

class ScientificWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
        'id',
        'first_name',
        'last_name',
        'patronymic',
        'rating',
        'scientific_work',
        'status',
        ]
        