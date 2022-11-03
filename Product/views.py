from django.shortcuts import render
from django.http import HttpResponse

from .models import Product

def index(request):
    # print(dir(request))
    return HttpResponse('<h1>Спискок тестів</h1>')

def test(request):
    #print(dir(request))
    return HttpResponse('<h1>Спискок тестів</h1>')

def dashboard(request):
    #print(dir(request))
    return HttpResponse('<h1>Dashboard SQL+Webhook</h1>')

def statistic(request):
    #print(dir(request))
    return HttpResponse('<h1>SQL Вибірка данних</h1>')

def config(request):
    #print(dir(request))
    return HttpResponse('Налаштування')