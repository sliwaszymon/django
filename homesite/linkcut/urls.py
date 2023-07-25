from django.urls import path

from .views import LinkcutIndexView, CutItFormView, LinkDetailView, LinkListView, LinkDeleteView, LinkStatisticsView, redirect_to

urlpatterns = [
    path("", LinkcutIndexView.as_view(), name="linkcut-index"),
    path("cutit/", CutItFormView.as_view(), name="cutit"),
    path("link/<pk>/", LinkDetailView.as_view(), name="link-detail"),
    path("links/", LinkListView.as_view(), name="link-list"),
    path("delete/<pk>/", LinkDeleteView.as_view(), name="link-delete"),
    path("r/<snippet>/", redirect_to, name="redirect"),
    path("statistics/", LinkStatisticsView.as_view(), name="link-statistics")
]
