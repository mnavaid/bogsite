from blog.models import BlogPosts
from django.contrib.auth import forms, authenticate, login, logout
from django.shortcuts import render,HttpResponseRedirect
from .forms import SignupForm, LoginForm
from django.contrib import messages


# Signup View
def signup(request):
  if request.method=="POST":
    frm = SignupForm(request.POST)
    if frm.is_valid():
      frm.save()
      messages.success(request, "Congratulations! Your Account has been created.")
  else:
    frm = SignupForm()
  return render(request,'users/signup.html',{'frm':frm})

# Login View
def user_login(request):
  if not request.user.is_authenticated:
    if request.method== 'POST':
      print("inside POST method")
      form = LoginForm(request=request, data= request.POST)
      if form.is_valid():
        uname = form.cleaned_data['username']
        upass = form.cleaned_data['password']
        user = authenticate(username=uname, password=upass)
        if user is not None:
          login(request, user)
          messages.success(request, "You have successfully logged in!!")
          return HttpResponseRedirect('/dashboard/')
        else: 
          messages.error(request, "Username or password is incorrect!!")
          #return HttpResponseRedirect(request,'users/login.html')
      else:
        messages.error(request, "Data you entered is incorrect!!")
    else:  
      form = LoginForm()
    return render(request,'users/login.html', {'form':form})
  else:
     return HttpResponseRedirect('/dashboard/')

# Logout View
def user_logout(request):
  logout(request)
  return HttpResponseRedirect('/')
