from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
#from .forms import ClientRegistrationForm,UserLoginForm

#from django.http.response import HttpResponse
# Create your views here.
 

def index(request):
    return render(request,'index.html')

def about_us(request):
    return render(request,'aboutus.html')

def contact_us(request):
    return render(request,'contactus.html')

def item(request):
    return render(request,'item.html')

def products(request):
    return render(request,'products.html')


def search(request):
    return render(request,'search.html')


#user_sign_up
def register(request):
    return render(request, 'signup.html')
"""  if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)  # Use your custom form if applicable
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)# Saves the user and creates the client profile automatically
            # Add any post-registration logic here (e.g., login the user)
            return redirect('login')  # Redirect to login page after registration
    else:
        form = ClientRegistrationForm()  # Use your custom form if applicable """
    


# login page
def login(request):
    """ if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to your home page
    else:
        form = UserLoginForm() """
    return render(request, 'login.html')


# logout page
def user_logout(request):
    logout(request)
    return redirect('login')
