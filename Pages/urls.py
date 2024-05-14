from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus', views.about_us, name='aboutus'),
    path('contactus', views.contact_us, name='contactus'),
    path('products', views.products, name='products'),
    path('login', views.login, name='login'),
    path('signup', views.register, name='signup'),
    path('item', views.item, name='item'),
    path('search', views.search, name='search'),
]
