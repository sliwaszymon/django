from django import forms
from django.forms.widgets import TextInput

from .models import Section, Todo


class SectionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'name',
            'name': 'name',
            'placeholder': 'Name of your section'
        })

        self.fields['todo_cap'].widget.attrs.update({
            'class': 'form-control',
            'id': 'todo_cap',
            'name': 'todo_cap',
            'aria-describedby': 'todo_cap_addon'
        })
        self.fields['todo_cap'].required = False

    class Meta:
        model = Section
        fields = ['name', 'todo_cap']


class TodoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'id': 'description',
            'name': 'description',
            'placeholder': 'Your\'s todo description'
        })

        self.fields['section'].widget.attrs.update({
            'class': 'form-control',
            'id': 'section',
            'name': 'section'
        })
        self.fields['section'].required = False

        self.fields['deadline'].widget.attrs.update({
            'class': 'form-control',
            'id': 'section',
            'name': 'section'
        })

        self.fields['color'].widget.attrs.update({
            'class': 'form-control form-control-color',
            'tittle': 'Choose your color',
            'id': 'color',
            'name': 'color',
            'size': '50'
        })

    class Meta:
        model = Todo
        fields = ['section', 'description', 'deadline', 'color']
        widgets = {
            'color': TextInput(attrs={'type': 'color'})
        }
