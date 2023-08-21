from django import forms

from .models import Link


class CutItForm(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['url'].widget.attrs.update({
            'class': 'form-control',
            'id': 'url',
            'name': 'url',
            'pattern': 'https://.*',
            'placeholder': 'https://www.yourlink.com'
        })
        self.fields['snippet'].widget.attrs.update({
            'class': 'form-control',
            'id': 'url',
            'name': 'url',
            'aria-describedby': 'snippet_addon'
        })
        self.fields['is_private'].widget.attrs.update({
            'class': 'form-check-input',
            'id': 'is_private',
            'name': 'is_private'
        })

    class Meta:
        model = Link
        fields = ['url', 'snippet', 'is_private']
