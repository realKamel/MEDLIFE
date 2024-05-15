

from django.contrib import messages

from django.shortcuts import render, redirect,get_object_or_404 
from .models import client , product_item
from django.contrib.auth import authenticate, login, logout # to handle user events
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import SignUpForm




#from .forms import ClientRegistrationForm,UserLoginForm

#from django.http.response import HttpResponse
# Create your views here.

def home(request):
    return render(request,'index.html')

def about_us(request):
    return render(request,'about_us.html')

def contact_us(request):
    return render(request,'contact_us.html')

def item(request,pk):
    all_products = product_item.objects.get(id=pk)
    return render(request,'item.html',{'all_products':all_products})

def products(request):
    all_products = product_item.objects.all()
    return render(request,'products.html',{'all_products':all_products})




def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request,("Logged out successfully :)"))
    return redirect('home')


def search(request):
    return render(request,'search.html')

def signup_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            user = authenticate(request, username=username, password=password)
            login(request,user)
            messages.success(request,("registed successfully :)"))
            return redirect('home')
        else:
            messages.success(request,("Error :)"))  
    else: 
        return render(request,'sign_up.html',{'form':form})

# login page

""" def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        if username and password:
            try:
                client = client.objects.get(username=username)
                if check_password(password, client.password):
                    request.session['client_id'] = client.id
                    messages.success(request, 'You have been successfully logged in.')
                    return redirect('index')
                else:
                    return render(request, 'login.html', {'error_message': 'Invalid Password'})
            except client.DoesNotExist:
                return render(request, 'login.html', {'error_message': 'Invalid Username'})
        else:
            messages.error(request, 'Please provide both username and password.')
    return render(request, 'login.html')
 """

""" def signup_view(request):
    pass
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            print(username)
            if client.objects.filter(username=username).exists():
                return render(request, 'signup.html', {'error_message': ' Username exists.'})
            else:
                hashed_password = make_password(form.cleaned_data['password'])
                client = client(
                    fullname=form.cleaned_data['fullname'],
                    username=username,
                    email=email,
                    phonenumber=form.cleaned_data['phonenumber'],
                    password=hashed_password
                )
                client.save()
                messages.success(request, 'your account has been created successful!.')
                return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

 """







""" def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username ,password)
        if username and password:
            try:
                client = client.objects.get(username=username)
                if (password == client.password):
                    request.session['client_id'] = client.id
                    return redirect('index')
                else:
                    return render(request, 'login.html', {'error_message': 'Invalid Password'})
            except client.DoesNotExist:
                return render(request, 'login.html', {'error_message': 'Invalid Username'})
        
    return render(request, 'login.html')

 """


#user_sign_up
""" def Client_register(request):
    if request.method == 'POST':
        form = Client_register_Form(request.POST)  # Use your custom form if applicable
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)# Saves the user and creates the client profile automatically
            # Add any post-registration logic here (e.g., login the user)
            return redirect('login')  # Redirect to login page after registration
    else:
        form = Client_register_Form()  # Use your custom form if applicable
        return render(request, 'signup.html') """
        
        
"""         
def Client_register(request):
    if request.method == 'POST':
        form = Client_register_Form(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page, or wherever you want
            return redirect('index')
    else:
        form = Client_register_Form()
    return render(request, 'signup.html', {'form': form})
 """


# logout page


""" 

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')  # Redirect to the homepage after login
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            # Optionally, you can create a user profile here
            # UserProfile.objects.create(user=new_user, ...)
            return redirect('login')  # Redirect to the login page after registration
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

 """
 