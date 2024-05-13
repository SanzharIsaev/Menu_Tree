from django.contrib import admin
from .models import Menu


@admin.register(Menu)
class Admin(admin.ModelAdmin):
    
    list_display = ['name', 'parent']    
    search_fields = ['name']
    list_filter = ['name']