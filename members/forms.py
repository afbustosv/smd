from django.forms import ModelForm
from .models import Member, Comment

class RegisterForm(ModelForm):
    class Meta:
        model = Member
        fields = ['tag', 'nick', 'serial', 'frase', 'pais', 'telefono', 'liga', 'refer']

class CommentForm(ModelForm):
    class Meta:
        model = Comment 
        fields =['description']
        
    def __init__(self):
        super().__init__()
        self.fields['description'].widget.attrs.update({'placeholder': 'Escribe un comentario',
                                                        'class': "form-control",
                                        })