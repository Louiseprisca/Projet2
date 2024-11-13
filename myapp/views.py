from asyncio import eager_task_factory

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Feature

# Create your views here.

def index(request):
    features = Feature.objects.all()
    return render (request, 'index.html',  {'features':features})

def register (request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2 :
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Cette adresse Mail est déjà utilisée !')
                return redirect('register')
            elif User.objects.filter(username = username).exists():
                messages.info(request, 'Ce nom d\'utilisateur est déjà pris !')
                return redirect('register')
            else :
                user = User.objects.create_user (username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else :
            messages.info(request, 'Les mots de passes sont différents !')
            return redirect('register')

    else:
        return render (request, 'register.html')

def login(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Informations Invalides !')
            return redirect('login')
    else :
        return render(request, 'login.html')

def blog (request):
    return render (request, 'blog.html')

def contact (request):
    return render (request, 'contact.html')

def portfolio (request):
    return render (request, 'portfolio.html')

def propos (request):
    return render (request, 'propos.html')

def services (request):
    return render (request, 'services.html')

def team (request):
    return render (request, 'team.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def counter (request):
    return render (request, 'counter.html')