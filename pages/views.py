from django import http
from django.shortcuts import render
from django.http import HttpResponse
from .models import Login
# Create your views here.

def index(request):
    x = {'name':'ali',
    'age':25}
    return render(request, 'pages/index.html', x)

def about(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    data = Login(username, password)
    data.save()
    
    return render(request, 'pages/about.html')   