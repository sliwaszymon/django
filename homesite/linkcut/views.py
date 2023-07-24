from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, TemplateView, FormView, CreateView, DeleteView
from .forms import CutItForm
from .models import Link


# Create your views here.

class IndexView(TemplateView):
    template_name = 'linkcut/index.html'


class CutItFormView(CreateView):
    template_name = 'linkcut/cutit.html'
    form_class = CutItForm
    model = Link


class LinkDetailView(DetailView):
    model = Link
    template_name = 'linkcut/link-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class LinkListView(ListView):
    model = Link
    template_name = 'linkcut/link-list.html'
    paginate_by = 100

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["now"] = timezone.now()
    #     return context


class LinkDeleteView(DeleteView):
    model = Link
    success_url = reverse_lazy('link-list')

# def redirect(request):
#     if request.method == "GET":
#         snippet = request.
