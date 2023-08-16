from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, DeleteView, UpdateView

from .forms import SectionForm, TodoForm
from .models import Section, Todo


@method_decorator(login_required, name='dispatch')
class TodosIndexView(TemplateView):
    template_name = 'todos/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sections = Section.objects.all()
        todos = Todo.objects.all()

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
            if todo_cap is not None:
                section.todo_cap = todo_cap
            else:
                section.todo_cap = 0
            section.save()
            return HttpResponseRedirect(reverse_lazy('todos-index'))

        if todo_form.is_valid():
            section = todo_form.cleaned_data['section']
            desc = todo_form.cleaned_data['description']
            deadline = todo_form.cleaned_data['deadline']
            color = todo_form.cleaned_data['color']
            todo = Todo(section=section, description=desc, deadline=deadline, color=color)
            todo.save()
            return HttpResponseRedirect(reverse_lazy('todos-index'))

        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


@method_decorator(login_required, name='dispatch')
class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todos/todo_update.html'
    success_url = reverse_lazy('todos-index')


@method_decorator(login_required, name='dispatch')
class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todos-index')


@method_decorator(login_required, name='dispatch')
class SectionDeleteView(DeleteView):
    model = Section
    success_url = reverse_lazy('todos-index')
