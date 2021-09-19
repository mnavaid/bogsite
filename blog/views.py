from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate
from .models import BlogPosts
from .forms import postForm
from django.contrib.auth.models import Group
from django.contrib import messages
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
  if request.user.is_authenticated:
    posts = BlogPosts.objects.all()
    usr = request.user
    uname =usr.get_full_name()
    grp = usr.groups.all()
    return render(request,'blog/dashboard.html', {'posts':posts, 'name':uname, 'group':grp})
  else:
    return HttpResponseRedirect('/login/')
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
        messages.success(request, "Post added successfully!!")
        return HttpResponseRedirect('/dashboard/')
    else:
      form=postForm()          
    return render(request, 'blog/addpost.html', {'form':form})
  else:
    return HttpResponseRedirect('/login/')


#Update Post View
def update_post(request,id):
  if request.user.is_authenticated:
    if request.method == 'POST':
      pi = BlogPosts.objects.get(pk=id)
      form = postForm(request.POST, instance=pi)
      if form.is_valid():
        form.save()
        messages.success(request, "Post updated successfully!!")
        return HttpResponseRedirect('/dashboard/')
    else:
      pi = BlogPosts.objects.get(pk=id)
      form = postForm(instance=pi)
    return render(request, 'blog/updatepost.html',{'form':form})
  else:
    return HttpResponseRedirect('/login/')

#Delete Post View
def delete_post(request,id):
  if request.user.is_authenticated:
    if request.method=='POST':
      pi = BlogPosts.objects.get(pk=id)
      pi.delete()
      messages.success(request, "Post Deleted successfully!!")
      return HttpResponseRedirect('/dashboard/')
  else:
    return HttpResponseRedirect('/login/')

