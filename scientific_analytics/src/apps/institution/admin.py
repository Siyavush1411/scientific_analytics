from django.contrib import admin
from .models import Institution

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution_type', 'phone', 'created_at')
    search_fields = ('name', 'address', 'phone')
    list_filter = ('institution_type', 'created_at')
