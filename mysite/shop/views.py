from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Inventory, Client


def inventory_list(request):
    inventories = Inventory.objects.all()
    context = {
        'inventories': inventories,
    }
    return render(request, 'shop/inventory_list.html', context)