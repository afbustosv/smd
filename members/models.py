from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Country(models.Model):
    pais = models.CharField(max_length=20)
    code = models.CharField(max_length=3, default=None)
    zona = models.CharField(max_length=30)
    indice = models.CharField(max_length=6)

    def __str__(self):
        return self.pais

class User(AbstractUser):
    miembro = models.BooleanField(default=False)

class League(models.Model):
    liga = models.CharField(max_length=20)

    def __str__(self):
        return self.liga

class Member(models.Model):
    nick = models.CharField(max_length=12)
    serial = models.CharField(max_length=6)
    frase = models.TextField(blank=True)
    pais = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    telefono = models.CharField(max_length=15)
    tag = models.BooleanField(default=False)
    liga = models.ForeignKey(League, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True)
    puntos = models.IntegerField(default=0)
    activo = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    refer = models.ForeignKey("Member", on_delete = models.CASCADE, blank=True, null=True)
    ip = models.GenericIPAddressField(null = True)

    def __str__(self):
        return self.nick