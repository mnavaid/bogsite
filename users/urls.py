from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('/', views.user_logout, name='logout'),
]
