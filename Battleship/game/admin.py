from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CreateUserForm
from .models import Player
from .models import Result


# Register your models here.

class MyUserAdmin(UserAdmin):
    add_form = CreateUserForm
    model = Player
    list_display = ['username', 'email', 'password', 'avatar']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('avatar', )}),
    )

admin.site.register(Player, MyUserAdmin)
admin.site.register(Result)