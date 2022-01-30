from time import perf_counter
from django.contrib import admin
from .models import Female, Male, User,Product,Video,Person
# Register your models here.

admin.site.register(Female)
admin.site.register(Male)
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Person)
admin.site.register(Video)
