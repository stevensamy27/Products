from os import name
from re import X
from unicodedata import category
from django.shortcuts import render
from .models import Product

# Create your views here.
def product(request):
    return render(request, 'product/product.html')

def products(request):
    a = Product.objects.all()
    x = {'pro':a}
    return render(request, 'product/products.html',x )



    ### some query set
    '''
    .all() >> show all products
    .filter() >> filter products by
    .order_by() >> To order Products by
    .count >> to count how many product on site  ## must write on string like [ str(a.count()) ]
    .exclude() show all products excluded some products

    '''

    ### some ranges in .filter() query set
    '''
    (name__exact = ' HE5O ')
    (name__contains = ' o ')
    (price__in = [0 , 10])
    (price__range = [0 , 10])


    '''