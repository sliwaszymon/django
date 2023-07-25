from django.http import HttpResponse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


def empty_response(request):
    return HttpResponse(status=204)
