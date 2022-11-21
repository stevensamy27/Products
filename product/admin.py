from itertools import product
from django.contrib import admin
from .models import Product, Test
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_display_link = ['price']
    list_editable = ['category']
    
    

admin.site.register(Product,  ProductAdmin) 
admin.site.register(Test)
admin.site.site_header = 'Nofal'
admin.site.site_title = 'BigNofal'
