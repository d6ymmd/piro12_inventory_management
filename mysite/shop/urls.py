from django.urls import path

from .views import inventory_list, inventory_create, inventory_detail, client_create, client_detail, client_list, \
    inventory_edit, inventory_delete, client_edit, client_delete

urlpatterns = [
    path('', inventory_list, name="inventory-list"),
    path('create/', inventory_create, name="inventory-create"),
    path('<int:pk>/', inventory_detail, name="inventory-detail"),
    path('<int:pk>/edit/', inventory_edit, name="inventory-edit"),
    path('<int:pk>/delete/', inventory_delete, name="inventory-delete"),
    path('client/', client_list, name="client-list"),
    path('client/create/', client_create, name="client-create"),
    path('client/<int:pk>/', client_detail, name="client-detail"),
    path('client/<int:pk>/edit/', client_edit, name="client-edit"),
    path('client/<int:pk>/delete/', client_delete, name="client-delete"),
]