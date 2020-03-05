from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, auth


# Create your views here.
def register(request):
    
    if request.method == 'POST':
        print('entered to loop')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if username == None:
            messages.info(request, 'username is empty')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username already taken')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email already registered')
        elif password1 != password2:
            messages.info(request, 'Password not matching')
        else:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                            password=password1, email=email)
            user.save()
            messages.info(request, 'User created')
            return redirect('accounts/login')
    else:
        return render(request, 'register.html')
    return render(request,'register.html')
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('')
        else:
            messages.info(request,'Invalid credentials')
    return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('')
