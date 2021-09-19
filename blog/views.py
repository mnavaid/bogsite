from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import BlogPosts
# Home View
def home(request):
  posts = BlogPosts.objects.all()
  return render(request,'blog/home.html', {'posts':posts})

# About View
def about(request):
  return render(request,'blog/about.html')

# Contact View
def contact(request):
  return render(request,'blog/contact.html')

# Dashboard View
def dashboard(request):
  posts = BlogPosts.objects.all()
  return render(request,'blog/dashboard.html', {'posts':posts})

