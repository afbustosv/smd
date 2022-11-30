from django.forms import ModelForm
from .models import Member

class RegisterForm(ModelForm):
    class Meta:
        model = Member
        fields = ['tag', 'nick', 'serial', 'frase', 'pais', 'telefono', 'liga']