from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Player
from .models import Result


class CreateUserForm(UserCreationForm):
    class Meta:
        model = Player
        fields = ['username', 'email', 'password1', 'password2', 'avatar']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'email'
        self.fields['password1'].widget.attrs['placeholder'] = 'password1'
        self.fields['password2'].widget.attrs['placeholder'] = 'password2'


class ResultForm(forms.ModelForm):
    fields = ['player1', 'player2']

    class Meta:
        model = Result
        fields = "__all__"
