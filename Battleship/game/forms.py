from django.contrib.auth.forms import UserCreationForm
from django import forms
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
    fields = ['mode', 'player1', 'player2', 'result1', 'result2', 'transcript1', 'transcript2']

    class Meta:
        model = Result
        fields = "__all__"


class VerifyPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(VerifyPasswordForm, self).clean()
        password = cleaned_data.get('password')