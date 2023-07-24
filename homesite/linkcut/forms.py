from django import forms
from .models import Link


class CutItForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['url'].widget.attrs['class'] = 'form-control'
        self.fields['url'].widget.attrs['type'] = 'url'
        self.fields['url'].widget.attrs['id'] = 'url'
        self.fields['url'].widget.attrs['name'] = 'url'
        self.fields['url'].widget.attrs['pattern'] = 'https://.*'
        self.fields['url'].widget.attrs['placeholder'] = 'https://www.yourlink.com'

        self.fields['snippet'].widget.attrs['class'] = 'form-control'
        self.fields['snippet'].widget.attrs['id'] = 'snippet'
        self.fields['snippet'].widget.attrs['name'] = 'snippet'
        self.fields['snippet'].widget.attrs['aria-describedby'] = 'snippet_addon'

    class Meta:
        model = Link
        fields = ['url', 'snippet']

    # url = forms.CharField(max_length=255, widget=forms.URLInput(
    #     attrs={
    #         'class': 'form-control',
    #         'id': 'url',
    #         'name': 'url',
    #         'placeholder': 'https://www.yourlink.com'
    #     }
    # ))
    # snippet = forms.CharField(max_length=20, widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control',
    #         'id': 'snippet',
    #         'name': 'snippet',
    #         'aria-describedby': 'snippet_addon'
    #     }
    # ))
    # creation_date = forms.DateTimeField()
    # visit_counter = forms.IntegerField()
