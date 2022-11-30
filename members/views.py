from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import RegisterForm
from .models import Member

# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        else:
            return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': 'Las contraseñas no coinciden'
            })


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if not user:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o Contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('home')


def members(request):
    members = Member.objects.all()
    return render(request, 'members.html', {
        'members' : members
    })


def signout(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', {
            'form': RegisterForm
        })
    else:
        try:
            form = RegisterForm(request.POST)
            new_player = form.save(commit=False)
            new_player.user = request.user
            new_player.save()
            return redirect('members')
        except ValueError:
            return render(request, 'register.html', {
            'form': RegisterForm,
            'error': 'Suministre datos válidos'
            })

    
