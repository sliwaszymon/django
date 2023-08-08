from django.views.generic import TemplateView, DeleteView
from django.urls import reverse_lazy

from .models import Section, Todo
from .forms import SectionForm, TodoForm


class TodosIndexView(TemplateView):
    template_name = 'todos/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sections = Section.objects.all()
        todos = Todo.objects.all()

        # todos = {}
        # for section in sections:
        #     todos[section.pk] = Todo.objects.filter(section=section)

        context['sections'] = sections
        context['todos'] = todos
        context['section_form'] = SectionForm()
        context['todo_form'] = TodoForm()
        return context

    def post(self, request, *args, **kwargs):
        section_form = SectionForm(request.POST)
        todo_form = TodoForm(request.POST)

        if section_form.is_valid():
            name = section_form.cleaned_data['name']
            todo_cap = section_form.cleaned_data['todo_cap']
            section = Section(name=name)
            if todo_cap != None:
                section.todo_cap = todo_cap
            else:
                section.todo_cap = 0
            section.save()

        if todo_form.is_valid():
            section = todo_form.cleaned_data['section']
            desc = todo_form.cleaned_data['description']
            deadline = todo_form.cleaned_data['deadline']
            color = todo_form.cleaned_data['color']
            todo = Todo(section=section, description=desc, deadline=deadline, color=color)
            todo.save()

        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todos-index')
