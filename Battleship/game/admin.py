from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CreateUserForm
from .models import Player


# Register your models here.

class MyUserAdmin(UserAdmin):
    add_form = CreateUserForm
    model = Player
    list_display = ['username', 'email', 'password', 'mobile_number']
    # fieldsets = UserAdmin.fieldsets + (None, {'fields': ('mobile_number',)})
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('mobile_number', )}),
    )

admin.site.register(Player, MyUserAdmin)
