from django.contrib import admin
from .models import Status
from django.contrib.admin import ModelAdmin


class ScientificWorkAdmin(ModelAdmin):
    model = Status
    
    list_display = (
        'id',
        'status_name'
    )
    

admin.site.register(Status, ScientificWorkAdmin)
