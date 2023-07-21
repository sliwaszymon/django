from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import ListView, DetailView, TemplateView, FormView, CreateView
from .forms import CutItForm
from .models import Link

# Create your views here.

class IndexView(TemplateView):
    template_name = 'linkcut/index.html'

class CutItFormView(CreateView):
    template_name = 'linkcut/cutit.html'
    form_class = CutItForm
    model = Link


# class LinkDetailView(DetailView):
#     model = Link
#     template_name = 'linkcut/link-detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         return context