from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('item', views.item, name='item'),
]
