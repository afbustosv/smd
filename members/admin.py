from django.contrib import admin
from .models import *

class MemberAdmin(admin.ModelAdmin):
    readonly_fields = ('created', )
# Register your models here.

admin.site.register(Country)
admin.site.register(League)
admin.site.register(Member, MemberAdmin)