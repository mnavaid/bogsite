from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate
from .models import BlogPosts
from .forms import postForm
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

#Add Post View
def add_post(request):
  if request.user.is_authenticated:
    if request.method=='POST':
      form = postForm(request.POST)
      if form.is_valid():
        title = form.cleaned_data['title']
        desc = form.cleaned_data['description']
        pst = BlogPosts(title=title, description=desc)
        pst.save()
        return HttpResponseRedirect('/dashboard/')
    else:
      form=postForm()          
    return render(request, 'blog/addpost.html', {'form':form})
  else:
    return HttpResponseRedirect('/login/')


#Update Post View
def update_post(request,id):
  if request.user.is_authenticated:
    return render(request, 'blog/updatepost.html')
  else:
    return HttpResponseRedirect('/login/')

#Delete Post View
def delete_post(request,id):
  if request.user.is_authenticated:
    return HttpResponseRedirect('/dashboard/')
  else:
    return HttpResponseRedirect('/login/')

