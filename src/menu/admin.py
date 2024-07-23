from django.contrib import admin
from .models import Menu

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu_name', 'parent', 'url', 'named_url')
    list_filter = ('menu_name',)
    search_fields = ('name',)

admin.site.register(Menu, MenuItemAdmin)