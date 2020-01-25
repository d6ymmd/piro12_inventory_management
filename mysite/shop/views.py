from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Inventory, Client


def inventory_list(request):
    inventories = Inventory.objects.all()
    context = {
        'inventories': inventories,
    }
    return render(request, 'shop/inventory_list.html', context)


def inventory_create(request):
    return render(request, 'shop/inventory_create.html')


def inventory_detail(request, pk):
    inventory = Inventory.objects.get(id=pk)
    return render(request, 'shop/inventory_detail.html', {'inventory': inventory})


def client_create(request):
    return render(request, 'shop/client_create.html')


def client_detail(request, pk):
    client = Client.objects.get(id=pk)
    return render(request, 'shop/client_detail.html', {'client': client})


def client_list(request):
    clients = Client.objects.all()
    context = {
        'clients': clients,
    }
    return render(request, 'shop/client_list.html', context)

