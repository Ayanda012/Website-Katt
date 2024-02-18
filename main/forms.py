from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from main.models import SolarTip
class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm (forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)