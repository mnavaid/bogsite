from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets

class SignupForm(UserCreationForm):
  password1 = forms.CharField(label='Password',  widget=forms.PasswordInput)
  password2 = forms.CharField(label='Re-Password',  widget=forms.PasswordInput)
  class Meta:
    model = User
    fields = ['username','first_name','last_name','email']
    labels = {'first_name':'First Name','last_name':'Last Name',
                'email':'Email'}
