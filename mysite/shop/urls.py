from django.urls import path

from .views import *

urlpatterns = [
    path('', inventory_list, name="inventory-list"),
    path('create/', inventory_create, name="inventory-create"),
    path('<int:pk>/', inventory_detail, name="inventory-detail"),
    path('<int:pk>/edit/', inventory_edit, name="inventory-edit"),
    path('<int:pk>/delete/', inventory_delete, name="inventory-delete"),
    path('<int:pk>/plus/', inventory_plus, name="inventory-plus"),
    path('<int:pk>/minus/', inventory_minus, name="inventory-minus"),
    path('client/', client_list, name="client-list"),
    path('client/create/', client_create, name="client-create"),
    path('client/<int:pk>/', client_detail, name="client-detail"),
    path('client/<int:pk>/edit/', client_edit, name="client-edit"),
    path('client/<int:pk>/delete/', client_delete, name="client-delete"),
]