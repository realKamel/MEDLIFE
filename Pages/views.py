from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

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


""" def log_in(request):
    return render(request,'log_in.html')
 """

""" def sign_up(request):
    return render(request,'sign_up.html') """


def products(request):
    return render(request,'products.html')



def search(request):
    return render(request,'search.html')


#user_sign_up
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'sign_up.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('index.html')
    else:
        form = LoginForm()
    return render(request, 'log_in.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')