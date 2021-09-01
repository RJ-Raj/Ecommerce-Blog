from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="BlogHome"),
    #path("blogpost/postComment/",views.postComment,name="postComment"),
    path("blogpost/<int:id>",views.blogpost,name="BlogPost"),
    path("signup/",views.handleSignup,name="handleSignup"),
    path("login/",views.handleLogin,name="handleLogin"),
    path("logout/",views.handleLogout,name="handleLogout"),
]