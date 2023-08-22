from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.views import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'username',
            'name': 'username',
            'placeholder': 'Username'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'password',
            'name': 'password',
            'placeholder': '*****'
        }
    ))


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'password',
            'name': 'password',
            'placeholder': '*****'
        }
    ))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'password2',
            'name': 'password2',
            'placeholder': '*****'
        }
    ))

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'id': 'username',
            'name': 'username',
        })
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'first_name',
            'name': 'first_name',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'id': 'email',
            'name': 'email',
        })

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords are not the same!')
        return cd['password2']
