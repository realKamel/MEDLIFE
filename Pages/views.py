from django.shortcuts import render
#from django.http.response import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')


def about_us(request):
    return render(request,'about_us.html')


def contact_us(request):
    return render(request,'contact_us.html')


def item(request):
    return render(request,'item.html')


def log_in(request):
    return render(request,'log_in.html')


def sign_up(request):
    return render(request,'sign_up.html')


def products(request):
    return render(request,'products.html')