from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us', views.about_us, name='about_us'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('products', views.products, name='products'),
    path('log_in', views.log_in, name='log_in'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('item', views.item, name='item'),
]
