from django.contrib import admin
from .models import ScientificWork
from django.contrib.admin import ModelAdmin


class ScientificWorkAdmin(ModelAdmin):
    model = ScientificWork
    
    list_display = (
        'id',
        'category',
        'author',
        'work_name',
        'work_rating',
        'uniquenes_score',
    )
    
    search_fields = ['category', 'author']

admin.site.register(ScientificWork, ScientificWorkAdmin)
