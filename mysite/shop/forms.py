from django import forms
from .models import Inventory, Client


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
