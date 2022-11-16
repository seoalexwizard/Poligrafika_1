from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', index),
    path('test/', test),
    path('dashboard/', dashboard),
    path('statistic/', statistic),
    path('config/', config),
    path('simple_function', views.simple_function)
]

