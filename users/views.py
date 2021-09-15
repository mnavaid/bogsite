from django.contrib.auth import forms
from django.shortcuts import render,HttpResponseRedirect
from .forms import SignupForm

# Signup View
def signup(request):
  frm = SignupForm()
  return render(request,'users/signup.html',{'frm':frm})

# Login View
def user_login(request):

  return render(request,'users/login.html')

# Login View
def user_logout(request):
  return HttpResponseRedirect('/')
