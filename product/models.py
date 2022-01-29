from distutils.command.upload import upload
from pickle import TRUE
from statistics import mode
from unicodedata import category, name
from django.db import models
from datetime import datetime

# Create your models here. (Your tables on fatabase)
class Product(models.Model):

    mylist = [
        ('phone', 'phone'),
        ( 'web','web')

    ]

    name  = models.CharField(max_length=60, verbose_name="title")
    content = models.TextField(null=TRUE , blank=True  , verbose_name="description")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to ='photos/%y/%m/%d')
    active = models.BooleanField(default=True) 
    category = models.CharField(max_length=50 , null=True, blank=True, choices=mylist)


    #To Show Name of Product on Admin Pannel  from "Product object (1)" >> to name of product
    def __str__(self) -> str:
        return self.name


    #Here just to change The name of feild from "ADD PRODUCT "  >> to "ADD PROoo" (NOT IMPORTANT)
    class Meta:
        verbose_name = 'Prooo'

    #TO sort products by name, price, any
    class Meta:
        ordering = ['name']




class Test(models.Model):
    date =  models.DateField()
    time = models.TimeField(null=True)
    created = models.DateTimeField(  default=datetime.now )