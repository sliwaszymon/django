from django.db.models import Count
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db.models.functions import ExtractYear, ExtractMonth, ExtractDay
from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView

from .utils import create_qr, qr_to_base64
from .forms import CutItForm
from .models import Link


class CutItFormView(CreateView):
    template_name = 'linkcut/cutit.html'
    form_class = CutItForm
    model = Link
    success_message = 'Link successfully cutted!'
    error_message = 'Shortcut or link has already been used.'

    def form_valid(self, form):
        value = form.cleaned_data
        print("Value of the input field:", value)
        return super().form_valid(form)

    def form_invalid(self, form):
        value = form.cleaned_data['url']
        link = Link.objects.filter(url=value)[:1].get()
        return redirect(reverse_lazy('link-detail', kwargs={"pk": link.pk}))

        # return super().form_invalid(form)


class LinkDetailView(DetailView):
    model = Link
    template_name = 'linkcut/link-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qr = create_qr(str('http://' + self.request.get_host() + '/r/linkcut/' + context['object'].snippet))
        context['qrcode'] = qr_to_base64(qr)
        return context


class LinkListView(ListView):
    model = Link
    template_name = 'linkcut/link-list.html'
    paginate_by = 10


class LinkDeleteView(DeleteView):
    model = Link
    success_url = reverse_lazy('link-list')


class LinkStatisticsView(TemplateView):
    template_name = 'linkcut/statistics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        top_records = list(Link.objects.filter(visit_counter__gt=0).order_by('-visit_counter'))

        top_records_labels = map(lambda x: str(x.snippet), top_records[:5])
        top_records_visits = map(lambda x: x.visit_counter, top_records[:5])
        all_visits = sum(map(lambda x: x.visit_counter, top_records))
        context['top_records_labels'] = list(top_records_labels)
        context['top_records_visits'] = list(top_records_visits)
        context['all_visits'] = all_visits

        date_counts = list(Link.objects.annotate(
            year=ExtractYear('creation_date'),
            month=ExtractMonth('creation_date'),
            day=ExtractDay('creation_date')
        ).values('year', 'month', 'day').annotate(link_count=Count('pk')))

        date_counts_refactored = [
            {
                'creation_date': f"{date['year']}-{date['month']}-{date['day']}",
                'link_count': date['link_count'],
            }
            for date in date_counts[:5]
        ]

        date_counts_labels = map(lambda x: str(x['creation_date']), date_counts_refactored)
        date_counts_data = map(lambda x: x['link_count'], date_counts_refactored)
        all_links = sum(map(lambda x: x['link_count'], date_counts))

        context['date_counts_labels'] = list(date_counts_labels)
        context['date_counts_data'] = list(date_counts_data)
        context['all_links'] = all_links

        return context


def redirect_to(request, snippet):
    link = Link.objects.get(snippet=snippet)
    link.visit_counter += 1
    link.save()
    return redirect(link.url)
