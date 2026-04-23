from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from authApp.models import *

def signup(req):
    if req.method=="POST":
        userType=req.POST.get('userType')
        fname=req.POST.get('fname')
        lname=req.POST.get('lname')
        email=req.POST.get('email')
        username=req.POST.get('username')
        password=req.POST.get('password')
        confirmPassword=req.POST.get('confirmPassword')
        gender=req.POST.get('gender')
        education=req.POST.get('education')
        
        if password==confirmPassword:
            user=custom_student.objects.create_user(username=username,password=password)
            user.first_name=fname
            user.last_name=lname
            user.email=email
            user.Gender=gender
            user.Education=education
            user.UserType=userType
            
            user.save()
            return redirect('signin')
        else:
            return redirect('signup')
    return render(req, 'signup.html')

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('dashboard')
        else:
            return redirect('signin')
    return render(request, 'signin.html')

def dashboard(request):
    return render(request, 'dashboard.html')