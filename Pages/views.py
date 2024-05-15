from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from .models import client
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password 
from django.contrib import messages





#from .forms import ClientRegistrationForm,UserLoginForm

#from django.http.response import HttpResponse
# Create your views here.

def home(request):
    return render(request,'index.html')

def about_us(request):
    return render(request,'about_us.html')

def contact_us(request):
    return render(request,'contact_us.html')

def item(request):
    return render(request,'item.html')

def products(request):
    return render(request,'products.html')


def search(request):
    return render(request,'search.html')

# login page

def login_view(request):
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


def signup_view(request):
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



def Client_logout(request):
    logout(request)
    return redirect('login')









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
 