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
            user=custom_student.objects.create_user(username=username,password=confirmPassword)
    return render(req, 'signup.html')