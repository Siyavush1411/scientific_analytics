from rest_framework import serializers
from .models import ScientificWork

class ScientificWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScientificWork
        fields = [
        'id',
        'category',
        'author',
        'work_name',
        'work_rating',
        'uniquenes_score',
        ]