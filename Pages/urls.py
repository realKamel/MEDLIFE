from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about_us', views.about_us, name='about_us'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('products', views.products, name='products'),
    path('login/', views.login_client, name='login'),
    path('signup', views.signup_view, name='signup'),
    path('item', views.item, name='item'),
    path('search', views.search, name='search'),
    path('logout/', views.logout_client, name='logout'),
]
