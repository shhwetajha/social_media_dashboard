from django.shortcuts import render,redirect
from django.contrib import auth
from .models import *
from django.contrib import messages
from mainapp.views import *
from django.contrib.auth.decorators import login_required
from mainapp.models import *


# Create your views here.

def view_signup(request):
    if request.method=='POST':
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password == confirm_password:
            if account.objects.filter(email=email).exists():
                messages.error(request,'email already exists')
                return redirect('signup')
            elif account.objects.filter(username=username).exists():
                messages.error(request,'username already exists')
                return redirect('signup')
            else:
                user=account.objects.create_user(email=email,username=username,password=password)
                user.is_active=True
                user.save()

                user_login=auth.authenticate(username=username,password=password)
                auth.login(request,user_login)
                userprofile=Profile.objects.create(user=user,id_user=user.id)
                userprofile.save()
                messages.success(request,'account has been successfully created')
                return redirect('setting')
        else:
            messages.error(request,'password and confirm password do not match')
            return redirect('signup')
    else:
        return render(request,'signup.html')

def view_signin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        print(email,password)
        userr=auth.authenticate(request,username=email,password=password)
        print(auth)
        print(userr)
        if userr is not None:
            # messages.success(request,'Account has been successfully logged in')
            auth.login(request,userr)
            return redirect('home')
        else:
            messages.error(request,'username or password not correct')
            return redirect('signin')
    else:
        return render(request,'signin.html')


@login_required(login_url='signin')
def view_logout(request):
    auth.logout(request)
    return redirect('signin')

@login_required(login_url='login')
def view_setting(request):
    Userprofile=Profile.objects.get(user=request.user)
    if request.method=='POST':
        if request.FILES.get('image') == None:
            image=Userprofile.profileimg
        else:
            image=request.FILES.get('image')
        bio=request.POST.get('bio')
        location=request.POST.get('location')

        Userprofile.profileimg=image
        Userprofile.bio=bio
        Userprofile.location=location
        Userprofile.save()
        return redirect('setting')
    context={'userprofile':Userprofile}
    return render(request,'setting.html',context)

@login_required(login_url='signin')
def view_profile(request,pk):
    user=account.objects.get(username=pk)
    userprofile=Profile.objects.get(user=user)
    posts=post.objects.filter(user=pk)
    posts_len=len(posts)
    context={'user':user,'userprofile':userprofile,'posts':posts,'posts_len':posts_len}
    return render(request,'profile.html',context)