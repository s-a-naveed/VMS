from django import forms
from django.contrib.auth.models import User
from .models import VehicleQualityCheck
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['username','email','password']
        widgets = {'password':forms.PasswordInput}
        error_messages ={
            'username':{'required':'Name is mandatory'},
            'email': {'required':'Email is mandatory'},
            'password':{'required':'Password is mandatory'},
        }

class LoginForm(forms.Form):
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {'password': forms.PasswordInput}


        