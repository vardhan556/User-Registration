from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def signuppage(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        print(uname,email,pass1,pass2)
        if pass1 != pass2:
            print("passwords doesnt match")
        else:
            if User.objects.filter(username=uname).exists():
                error="user id exists"
                return render(request,'signup.html',{'error':error})
            elif User.objects.filter(email=email).exists():
                error="email id exists"
                return render(request,'signup.html',{'error':error})
            else:
                my_user=User.objects.create_user(uname,email,pass1)
                my_user.save()
                return redirect('loginpage')
    return render(request,'signup.html')


def loginpage(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        passw=request.POST.get('password')
        user=authenticate(request,username=uname,password=passw)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            error2="wrong credentials entered"
            return render(request,'login.html',{'error2':error2})
    return render(request,'login.html')


@login_required(login_url='login')
def homepage(request):
    return render(request,'homepage.html')

def logoutpage(request):
    logout(request)
    return redirect('loginpage')
