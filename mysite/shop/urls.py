from django.urls import path

from .views import inventory_list, inventory_create, inventory_detail, client_create, client_detail, client_list

urlpatterns = [
    path('', inventory_list, name="inventory-list"),
    path('create/', inventory_create, name="inventory-create"),
    path('<int:pk>/', inventory_detail, name="inventory-detail"),
    path('client/', client_list, name="client-list"),
    path('client/create/', client_create, name="client-create"),
    path('client/<int:pk>/', client_detail, name="client-detail"),
]