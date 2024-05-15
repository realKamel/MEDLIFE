from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus', views.about_us, name='about_us'),
    path('contactus', views.contact_us, name='contactus'),
    path('products', views.products, name='products'),
    path('login', views.login_view, name='login'),
    path('signup', views.signup_view, name='signup'),
    path('item', views.item, name='item'),
    path('search', views.search, name='search'),
]
