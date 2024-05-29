from django.contrib import admin
from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ["slug"]
    search_fields = ['title', 'content']

admin.site.register(Service, ServiceAdmin)