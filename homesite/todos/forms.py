from django import forms

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
            'placeholder': 'Live empty for no limits'
        })

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
            'placeholder': 'Name of your section'
        })

        self.fields['section'].widget.attrs.update({
            'class': 'form-control',
            'id': 'section',
            'name': 'section'
        })

        self.fields['deadline'].widget.attrs.update({
            'class': 'form-control',
            'id': 'section',
            'name': 'section'
        })

    class Meta:
        model = Todo
        fields = ['section', 'description', 'deadline', 'color']
