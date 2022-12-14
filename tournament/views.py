from django.shortcuts import render
from django.template.defaulttags import register
from .models import Tournament

# Create your views here.

def tournaments(request):
    tournament = Tournament.objects.all()
    return render(request, 'tournaments.html', {
        'tournaments': tournament
    })

def tournament(request, id):
    tournament = Tournament.objects.get(pk = id)
    return render(request, 'tournament.html',{
        'tournament': tournament
    })

@register.filter
def get_range(value):
    return range(value)

@register.filter
def module(value):
    return value%2

@register.filter
def half(value):
    return value//2

@register.filter  
def mayus(value):
    return value.capitalize()

@register.filter
def fecha(value):
    if value == None:
        return "--/--/--"
    else:
        return str(value.day) +'/'+ str(value.month) +'/'+ str(value.year)[2:]