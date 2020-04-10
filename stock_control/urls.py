from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.stock_list, name='stock_list'),
    path('category/new/', views.category_add, name='category_add'),
]