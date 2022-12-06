from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('member', 'registro')
    

class MemberAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'ip' )
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('date', )

admin.site.register(Country)
admin.site.register(League)
admin.site.register(User, UserAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Member, MemberAdmin)