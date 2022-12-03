from django.urls import path, include
from .views import *
from . import views
from Product.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'productlist', ProductViewSet )
print(router.urls)

urlpatterns = [
    path('', index),
    path('test/', test),
    path('dashboard/', dashboard),
    path('statistic/', statistic),
    path('config/', config),
    path('simple_function', views.simple_function),
    path('api/v1/', include(router.urls)),
    #path('api/v1/productlist/', ProductAPIList.as_view()),
    #path('api/v1/productlist/<int:pk>/', ProductAPIUpdate.as_view()),
    #path('api/v1/productdetail/<int:pk>/', ProductAPIDetailView.as_view()),
]

