from django.db import models
from django.utils.timezone import datetime

# Create your models here.

class Tournament(models.Model):
    TIPO = (
        ('C', 'Copa'),
        ('L', 'Liga'),
        ('M', 'Mix'),
    )
    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=5, choices=TIPO)
    premio = models.CharField(max_length=20)
    couta = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    inicio = models.DateTimeField(null=True)
    final = models.DateTimeField(null=True)
    numero = models.SmallIntegerField(default=8)

    def __str__(self):
        return self.nombre