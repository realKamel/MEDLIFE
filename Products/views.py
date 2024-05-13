from django.shortcuts import render
from .models import product_item

# Create your views here.
def products(request):
    return render(request,'Products/products.html')


def item(request):
    return render(request,'Products/item.html')