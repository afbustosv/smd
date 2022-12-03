from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.template.defaulttags import register
from .forms import RegisterForm
import datetime 
from .models import Member, User

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
            member = Member.objects.get(user = request.user)
            if member:
                member.last_login = datetime.date.today()
                member.ip = request.META.get('REMOTE_ADDR')
                member.save()
            return redirect('home')


def members(request):
    members = Member.objects.all().order_by('-puntos')
    return render(request, 'members.html', {
        'members': members
    })


def profile(request, id):
    member = Member.objects.get(pk=id)
    return render(request, 'profile.html', {
        'member': member
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
            user = User.objects.get(username = request.user)
            print(user)
            user.miembro = True
            user.save()
            return redirect('members')
        except ValueError:
            return render(request, 'register.html', {
                'form': RegisterForm,
                'error': 'Suministre datos válidos'
            })
