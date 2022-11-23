from django.urls import path
from .views import *
from . import views
from Product.views import ProductAPIView

urlpatterns = [
    path('', index),
    path('test/', test),
    path('dashboard/', dashboard),
    path('statistic/', statistic),
    path('config/', config),
    path('simple_function', views.simple_function),
    path('api/v1/productlist/', ProductAPIView.as_view())
]

