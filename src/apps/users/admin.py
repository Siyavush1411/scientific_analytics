from django.contrib import admin
from .models import User
from django.contrib.admin import ModelAdmin


class UserAdmin(ModelAdmin):
    model = User
    
    list_display = (
        'id',
        'first_name',
        'last_name',
        'patronymic',
        'rating',
        'status',
    )
    search_fields = ['scientific_work', 'status',]

admin.site.register(User, UserAdmin)
