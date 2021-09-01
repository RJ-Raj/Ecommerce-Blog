from django.shortcuts import render,redirect
from .models import Blogpost
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



def index(request):
    myposts = Blogpost.objects.all()
    return render(request,"blog/index.html",{"myposts":myposts})

def blogpost(request,id):
    post = Blogpost.objects.filter(post_id=id).first()
    return render(request,"blog/blogpost.html",{"post":post})

def handleSignup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        fullname = request.POST['fullname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 != pass2:
            messages.error(request,"Your password does not match.")
            return redirect('/blog')
        else:
            myuser = User.objects.create_user(username,email,pass1)
            myuser.first_name = fullname
            myuser.save()
            messages.success(request,"Your request is submitted successfully.")
            return redirect('/blog')
    else:
        return HttpResponse("404- Not Found")

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginemail']
        lpass = request.POST['pass']

        user = authenticate(request,username=loginusername,password= lpass)
        if user is not None:
            login(request,user)
            messages.success(request,"You have successfully Logged in")
            return redirect('/blog')    
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/blog')
    return HttpResponse("404- Not Found")


def handleLogout(request):
        logout(request)
        messages.success(request,"You have successfully Logged Out")
        return redirect('/blog')