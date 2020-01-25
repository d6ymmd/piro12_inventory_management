from django.shortcuts import render

from django.http import HttpResponse


def inventory_list(request):
    return HttpResponse("Hello, world. You're at the shop inventory_list.")