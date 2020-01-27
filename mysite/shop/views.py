from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Inventory, Client
from .forms import InventoryForm, ClientForm


def inventory_list(request):
    inventories = Inventory.objects.all()
    return render(request, 'shop/inventory_list.html', {'inventories': inventories, })


# def inventory_stock(request, stock_plus, stock_minus):
#     inventory =
#     stock = inventory.stock
#     if stock_plus:
#         stock += 1
#         stock.save()
#     elif stock_minus:
#         return stock -= 1

# def stock_edit(request):
#     inventory = Inventory.objects.all()
#     if inventory.stock >= 0:
#         if:
#             inventory.stock += 1
#             inventory.save()
#         else:
#             inventory.stock -= 1
#             inventory.save()
#
#         return redirect('inventory-list')
#     return render(request, 'shop/inventory-detail.html', {'inventory':inventory, })
#

def inventory_create(request, inventory=None):
    if request.method == 'POST':
        form = InventoryForm(request.POST, request.FILES, instance=inventory)
        if form.is_valid():
            inventory = form.save()
            return redirect('inventory-list')
    else:
        form = InventoryForm(instance=inventory)
    return render(request, 'shop/inventory_create.html', {'form': form, })


def inventory_edit(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    return inventory_create(request, inventory)


def inventory_delete(request, pk):
    inventory = Inventory.objects.get(id=pk)
    inventory.delete()
    return redirect('inventory-list')


def inventory_detail(request, pk):
    inventory = Inventory.objects.get(id=pk)
    return render(request, 'shop/inventory_detail.html', {'inventory': inventory, })


def client_create(request, client=None):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            client = form.save()
            return redirect('client-list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'shop/client_create.html', {'form': form, })


def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return client_create(request, client)


def client_delete(request, pk):
    client = Client.objects.get(id=pk)
    client.delete()
    return redirect('client-list')


def client_detail(request, pk):
    client = Client.objects.get(id=pk)
    inventories = Inventory.objects.all()
    return render(request, 'shop/client_detail.html', {'client': client, 'inventories': inventories, })


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'shop/client_list.html', {'clients': clients, })

