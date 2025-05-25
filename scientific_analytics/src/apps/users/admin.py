from django.contrib import admin
from .models import User
from django.contrib.admin import ModelAdmin
from apps.users.utils.synchronize_users import synch, synch_scientific_works

class UserAdmin(ModelAdmin):
    model = User
    actions = ['synch_authors']
    
    @admin.action(description='Синхронизировать авторов')
    def synch_authors(self, request, queryset):
        synch_scientific_works()
        self.message_user(request, "Авторы синхронизированы")
    
    list_display = (
        'id',
        'first_name',
        'last_name',
        'patronymic',
        'rating',
        'status',
        'created_at',
        'update_at',
    )
    search_fields = ['scientific_work', 'status',]

admin.site.register(User, UserAdmin)
