import time, datetime, os

from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import errno
import os


def index(request):
    product = Product.objects.order_by('-created_at')
    return render(request, 'Product/index.html', {'product': product, 'order_id': 'Список Product'})

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

def home(request):
    context = {
        'title': 'Trigger python logic'
    }
    return render(request, 'home/home.html', context)


def simple_function(request):
    import zipfile
    import shutil
    import os
    import sys


    os.chdir('D:\Poligrafika\Poligrafika\media')
    file_zip = zipfile.ZipFile('order-item-357146.zip', 'r')
    file_zip.extractall('./')
    for file_info in file_zip.infolist():
        print(file_info.filename, file_info.date_time, file_info.file_size)

    file_zip.close()

    file_zip = ['views.py', 'order-item-357146.zip']
    for file in file_zip:
        print(file, zipfile.is_zipfile(file))

    directory = r'D:\Poligrafika\Poligrafika\media'


    paper = r'D:\Poligrafika\Poligrafika\media\Папір\350'
    original = ('D:\Poligrafika\Poligrafika\media\Оригінал/%Y/%m/%d')
    arhiv = r'D:\Poligrafika\Poligrafika\media\Архив'
    date = r'/%Y/%m/%d/'
    for file in os.listdir(directory):
        ext = os.path.splitext(file)[1]
        if not os.path.exists (directory):
            os.mkdir(directory)
        match ext.lower():
            case '.pdf':
                shutil.move(src=rf'{directory}\{file}', dst=paper)
            case '.zip':
                shutil.move(src=rf'{directory}\{file}', dst=arhiv)
        folder = datetime.date.today()
        try:
            os.makedirs(folder.strftime("Оригінал/%Y/%m/%d"), exist_ok=False)
        except (FileExistsError):
            print(" File or directory is already exists")
        except (FileNotFoundError):
            print(" Path is not correct ")
        except OSError:
            print("Failed to create  %s " % folder)
        else:
            print("Successfully created the directory %s " % folder)




    return HttpResponse('''<html><script>window.location.replace('/');</script></html>''')
