from django import forms
from .models import Link

class CutItForm(forms.Form):
    url = forms.CharField(max_length=255, widget=forms.URLInput(
        attrs={
            'class': 'form-control',
            'id': 'url',
            'name': 'url',
            'placeholder': 'https://www.yourlink.com'
        }
    ))
    snippet = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'snippet',
            'name': 'snippet',
            'aria-describedby': 'snippet_addon'
        }
    ))
    creation_date = forms.DateTimeField()
    visit_counter = forms.IntegerField()
