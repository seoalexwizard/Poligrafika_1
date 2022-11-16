from django.shortcuts import render
from django.http import HttpResponse

from .models import Product

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

    file_zip = zipfile.ZipFile('order-item-357146.zip', 'r')

    file_zip.extractall('./')
    for file_info in file_zip.infolist():
        print(file_info.filename, file_info.date_time, file_info.file_size)

    file_zip.close()

    file_zip = ['main.py', 'order-item-357146.zip']
    for file in file_zip:
        print(file, zipfile.is_zipfile(file))

    directory = r'D:\Poligrafika'

    paper = r'D:\Poligrafika\Папір'
    original = r'D:\Poligrafika\Оригінал'
    arhiv = r'D:\Poligrafika\Архив'

    for file in os.listdir(directory):
        ext = os.path.splitext(file)[1]
        match ext.lower():
            case '.pdf':
                shutil.move(src=rf'{directory}\{file}', dst=paper)
            case '.zip':
                shutil.move(src=rf'{directory}\{file}', dst=arhiv)
    shutil.move(src=rf'{original}\{file}', dst=original)

    shutil.rmtree('originals')
    return HttpResponse('''<html><script>window.location.replace('/');</script></html>''')
