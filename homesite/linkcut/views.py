from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView, FormView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'linkcut/index.html'