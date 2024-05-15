
from django import forms




class SignUpForm(forms.Form):
    fullname = forms.CharField(max_length=100)
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    phonenumber = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput)



""" from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import client


class Client_register_Form(UserCreationForm):
    class Meta:
        model = client
        fields = ['username', 'email','password','email']


class Client_login_Form(AuthenticationForm):
    class Meta:
        model = client
        fields = ['username', 'password']
        
        

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email','password','email']

    def clean_password2(self):
        # Check if the two password entries match
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2 """