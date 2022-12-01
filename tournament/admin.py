from django.contrib import admin
from .models import *

class TournamentAdmin(admin.ModelAdmin):
    readonly_fields = ('created', )

# Register your models here.
admin.site.register(Tournament, TournamentAdmin)