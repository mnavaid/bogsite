from django.http.response import HttpResponseRedirect
from django.shortcuts import render

# Home View
def home(request):
  return render(request,'blog/home.html')

# About View
def about(request):
  return render(request,'blog/about.html')

# Contact View
def contact(request):
  return render(request,'blog/contact.html')

# Dashboard View
def dashboard(request):
  return render(request,'blog/dashboard.html')

