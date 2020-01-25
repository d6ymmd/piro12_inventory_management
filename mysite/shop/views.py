from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Inventory, Client


def inventory_list(request):
    inventory = Inventory.objects.all()
    data = {
        'inventory': inventory
    }
    return render(request, 'shop/inventory_list.html', data)