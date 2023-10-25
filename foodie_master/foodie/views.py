from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User

def home(request):
    return render(request, 'index.html' )

def register_view(request):
    
        if request.method == "POST":
            username = request.POST['uname']
            pass1 = request.POST['psw']
            pass2 = request.POST['psw-repeat']
            print(username)
            if pass1 != pass2:
                messages.error(request,"Password didn't match!")
            else:
                myuser = User.objects.create_user(username=username, password=pass1)
                myuser.is_active=True
                myuser.save()
                return redirect('/login')
        return render(request, "sign-up.html")


    

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None: 
            return redirect('http://localhost:63342/chatbotfood/foodie-master/index.html?_ijt=3mvcr5777d2hdfp9hogm52nj56')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'login.html')
