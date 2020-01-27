import re
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Inventory, Client
from .forms import InventoryForm, ClientForm


def inventory_list(request):
    inventories = Inventory.objects.all()
    return render(request, 'shop/inventory_list.html', {'inventories': inventories, })


def inventory_create(request, inventory=None):
    if request.method == 'POST':
        form = InventoryForm(request.POST, request.FILES)
        if form.is_valid():
            inventory = form.save()
            return redirect('inventory-list')
    else:
        form = InventoryForm()
    return render(request, 'shop/inventory_create.html', {'form': form, })


def inventory_detail(request, pk):
    inventory = Inventory.objects.get(id=pk)
    return render(request, 'shop/inventory_detail.html', {'inventory': inventory, })


def client_create(request, client=None):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save()
            return redirect('client-list')
    else:
        form = ClientForm()
    return render(request, 'shop/client_create.html', {'form': form, })


def client_detail(request, pk):
    client = Client.objects.get(id=pk)
    inventories = Inventory.objects.all()
    return render(request, 'shop/client_detail.html', {'client': client, 'inventories': inventories, })


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'shop/client_list.html', {'clients': clients, })

