from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
        'id',
        'category',
        'author',
        'work_name',
        'work_rating',
        'uniquenes_score',
        ]