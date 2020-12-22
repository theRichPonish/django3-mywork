from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.authentication, name='authentication'),
    path('signup/', views.signupuser, name = "signupuser"),
    path('signin/', views.signinuser, name = "signinuser"),
    path('signout/', views.signoutuser, name = "signoutuser"),
    path('userdetails/', views.userdetails, name = "userdetails"),
    path('changepassword/', views.changepassword, name = "changepassword"),
]
