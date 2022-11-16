#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Poligrafika.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()


import zipfile
import shutil
import os

file_zip = zipfile.ZipFile('order-item-357146.zip', 'r')

file_zip.extractall('./')
for file_info in file_zip.infolist():
    print(file_info.filename, file_info.date_time, file_info.file_size)

file_zip.close()

file_zip = ['manage.py', 'order-item-357146.zip']
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