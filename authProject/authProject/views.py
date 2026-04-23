from django.shortcuts import render,redirect
from authApp.models import *

def signup(req):
    if req.method=="POST":
        userType=req.POST.get('userType')
        fname=req.POST.get('fname')
        lname=req.POST.get('lname')
        username=req.POST.get('username')
        email=req.POST.get('email')
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
            return redirect('login')
        else:
            return redirect('signup')
    return render(req, 'signup.html')

def signin(request):
    return render(request, 'login.html')