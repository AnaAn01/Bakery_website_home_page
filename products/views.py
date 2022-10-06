from django.shortcuts import render

from django.http import HttpResponse
from .models import Product

def catalog(request):
    return render(request, 'products/catalog.html')


def cart(request):
    return HttpResponse("It is a cart with your orders")