from django.contrib import admin
from .models import *

# Register your models here.
class Useradmin(admin.ModelAdmin):
    class Meta:
        model=account
        fields='__all__'


class UserProfileAdmin(admin.ModelAdmin):
    class Meta:
        model=Profile
        fields='__all__'

admin.site.register(account,Useradmin)
admin.site.register(Profile,UserProfileAdmin)

