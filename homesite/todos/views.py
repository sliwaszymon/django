from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, DeleteView, UpdateView

from .forms import SectionForm, TodoForm, BoardForm
from .models import Section, Todo, Board


@method_decorator(login_required, name='dispatch')
class BoardsView(TemplateView):
    template_name = 'todos/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_boards = Board.objects.filter(owner=self.request.user)
        public_boards = Board.objects.filter(is_private=False).exclude(owner=self.request.user)

        context['my_boards'] = my_boards
        context['public_boards'] = public_boards
        context['form'] = BoardForm()

        return context

    def post(self, request, *args, **kwargs):
        form = BoardForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            is_private = form.cleaned_data['is_private']

            board = Board(name=name, is_private=is_private, owner=request.user)
            board.save()
            return HttpResponseRedirect(reverse_lazy('todos-index'))

        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


@method_decorator(login_required, name='dispatch')
class BoardDeleteView(DeleteView):
    model = Board
    success_url = reverse_lazy('todos-index')


@method_decorator(login_required, name='dispatch')
class TodosView(TemplateView):
    template_name = 'todos/board.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        sections = Section.objects.filter(board=pk)
        unsigned_todos = Todo.objects.filter(board=pk, section=None)

        todo_form = TodoForm()
        todo_form.fields['section'].queryset = sections

        context['board_pk'] = pk
        context['sections'] = sections
        context['unsigned_todos'] = unsigned_todos
        context['section_form'] = SectionForm()
        context['todo_form'] = todo_form
        return context

    def post(self, request, *args, **kwargs):
        section_form = SectionForm(request.POST)
        todo_form = TodoForm(request.POST)

        context = self.get_context_data(*args, **kwargs)
        board_pk = context['board_pk']

        if section_form.is_valid():
            name = section_form.cleaned_data['name']
            todo_cap = section_form.cleaned_data['todo_cap']
            section = Section(name=name)
            section.board = Board.objects.get(pk=board_pk)
            if todo_cap is not None:
                section.todo_cap = todo_cap
            else:
                section.todo_cap = 0
            section.save()
            return HttpResponseRedirect(reverse_lazy('board', kwargs={'pk': board_pk}))

        if todo_form.is_valid():
            section = todo_form.cleaned_data['section']
            desc = todo_form.cleaned_data['description']
            deadline = todo_form.cleaned_data['deadline']
            color = todo_form.cleaned_data['color']
            todo = Todo(section=section, description=desc, deadline=deadline, color=color)
            todo.board = Board.objects.get(pk=board_pk)
            todo.save()
            return HttpResponseRedirect(reverse_lazy('board', kwargs={'pk': board_pk}))

        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


@method_decorator(login_required, name='dispatch')
class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todos/todo_update.html'

    def get_success_url(self):
        board_pk = self.kwargs['board_pk']
        return reverse_lazy('board', kwargs={'pk': board_pk})


@method_decorator(login_required, name='dispatch')
class TodoDeleteView(DeleteView):
    model = Todo

    def get_success_url(self):
        board_pk = self.kwargs['board_pk']
        return reverse_lazy('board', kwargs={'pk': board_pk})


@method_decorator(login_required, name='dispatch')
class SectionDeleteView(DeleteView):
    model = Section

    def get_success_url(self):
        board_pk = self.kwargs['board_pk']
        return reverse_lazy('board', kwargs={'pk': board_pk})
