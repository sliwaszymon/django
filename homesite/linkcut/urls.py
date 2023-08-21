from django.urls import path
from django.views.generic.base import RedirectView

from .views import CutItFormView, LinkDetailView, LinkListView, MyLinkListView, LinkDeleteView, LinkStatisticsView, redirect_to

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="cutit", permanent=True)),
    path("cutit/", CutItFormView.as_view(), name="cutit"),
    path("link/<pk>/", LinkDetailView.as_view(), name="link-detail"),
    path("links/", LinkListView.as_view(), name="link-list"),
    path("links/my/", MyLinkListView.as_view(), name="my-link-list"),
    path("delete/<pk>/", LinkDeleteView.as_view(), name="link-delete"),
    path("r/<snippet>/", redirect_to, name="redirect"),
    path("statistics/", LinkStatisticsView.as_view(), name="link-statistics")
]
