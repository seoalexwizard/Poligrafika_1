from django.urls import path
from .views import *
from . import views
from Product.views import *

urlpatterns = [
    path('', index),
    path('test/', test),
    path('dashboard/', dashboard),
    path('statistic/', statistic),
    path('config/', config),
    path('simple_function', views.simple_function),
    path('api/v1/productlist/', ProductAPIList.as_view()),
    path('api/v1/productlist/<int:pk>/', ProductAPIList.as_view()),
]

