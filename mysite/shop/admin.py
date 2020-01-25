from django.contrib import admin

from .models import Client, Inventory

admin.site.register(Client)
admin.site.register(Inventory)
