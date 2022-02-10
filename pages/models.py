from pickle import TRUE
from tkinter import CASCADE
from traceback import print_exception
from django.db import models

# Create your models here.

##### RELATIONSHIPS BETWEEN TABLES
# ONE TO ONE 
# ONE TO MANY
# MANY TO MANY



# Example about ONE TO ONE relationship

class Female(models.Model):
    name_female = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return self.name_female

    
class Male(models.Model):
    name_male = models.CharField(max_length=50, null=True)
    relation = models.OneToOneField(Female, on_delete=models.CASCADE)  
    def __str__(self) -> str:
        return self.name_male         




##########################################################################################


# Example about ONE TO MANY relationship
   
class Product(models.Model):
    title = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return self.title

class User(models.Model):
    name = models.CharField(max_length=50, null=True)
    relastion = models.ForeignKey(Product , on_delete=models.CASCADE )
    def __str__(self) -> str:
        return self.name


##########################################################################################

# Example about MANY TO MANY relationship
   
class Video(models.Model):
    title = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return self.title

class Person(models.Model):
    name = models.CharField(max_length=50, null=True)

    relation = models.ManyToManyField(Video, null=True)
    def __str__(self) -> str:
        return self.name 


class Login(models.Model):
    
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)