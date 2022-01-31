from os import name
from re import X
from django.shortcuts import render
from .models import Product

# Create your views here.
def product(request):
    return render(request, 'product/product.html')

def products(request):
    x = {'pro':Product.objects.all().filter(name = 'apple 123')}
    return render(request, 'product/products.html',x )