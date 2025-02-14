from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import ContactForm
# Create your views here.

def SignupPage(request):
    if request.method =='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')

        if User.objects.filter(email=email).exists():
            messages.error(request,'Email Already Exists!')
            return redirect('Signup')
        else:
            obj=User.objects.create_user(name,email,password)
            obj.save()
            return redirect('Signin')

    return render (request,'Signup.html')


def LoginPage(request):
    if request.method =='POST':
        uname=request.POST.get('name')
        pass1=request.POST.get('pass')
        print(uname,pass1)
        user=authenticate(request,username=uname,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        
        else:
            messages.error(request,'Incorrect Username or Passoword')
            return redirect('Signin')

    return render (request,'Signin.html')   
    
   

def HomePage(request):
    return render (request,'home.html')

def ForgetPassword(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        newpass = request.POST.get('newpass')
        confpass = request.POST.get('confpass')

        user = User.objects.filter(username__iexact=username).first()
        if not user:
            messages.error(request, 'Invalid username or user not found')
            return redirect('forgetpassword')


        if newpass != confpass:
          
            messages.error(request, 'Passwords do not match')
            return redirect('forgetpassword')
        
        # if len(newpass) < 8:
        #     messages.error(request, 'Password should be at least 8 characters long')
        #     return redirect('forgetpassword')

       
        user.set_password(newpass)
        user.save()

        
        messages.success(request, 'Password changed successfully.')
        return redirect('Signin')

    return render(request, 'forgetpassword.html')


def Show_Username(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user = User.objects.filter(username__iexact=username).first()

    return render(request, 'home.html', {'user': user})


def Logout(request):
    logout(request)
    return redirect('Signin')


def Contact(request):
    if request.method == 'POST':
        nme = request.POST.get('name')
        eml = request.POST.get('email')
        msg = request.POST.get('message')
        
        # Create a ContactForm instance and save it
        contact_form = ContactForm(name=nme, email=eml, message=msg)
        contact_form.save()
        
        return redirect('home')  # Redirect to the desired page after form submission

    return render(request, 'home.html')