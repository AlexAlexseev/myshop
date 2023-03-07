#from django.conf.urls import url
from django.urls import re_path
from django.urls import path

from . import views

app_name = 'shop'


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<slug:category_slug>/<int:id>/', views.product_detail, name='product_detail'),
]
