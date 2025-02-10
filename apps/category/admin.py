from django.contrib import admin
from .models import Category
from django.contrib.admin import ModelAdmin


class CategoryAdmin(ModelAdmin):
    model = Category
    
    list_display = (
        'id',
        'category_name',
    )
    

admin.site.register(Category, CategoryAdmin)
