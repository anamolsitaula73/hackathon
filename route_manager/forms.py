# route_manager/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class RouteManagerLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
