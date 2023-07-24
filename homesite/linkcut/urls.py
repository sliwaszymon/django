from django.urls import path
from .views import IndexView, CutItFormView, LinkDetailView, LinkListView, LinkDeleteView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("cutit/", CutItFormView.as_view(), name="cutit"),
    path("link/<pk>/", LinkDetailView.as_view(), name="link-detail"),
    path("links/", LinkListView.as_view(), name="link-list"),
    path("delete/<pk>/", LinkDeleteView.as_view(), name="link-delete")
    # path("redirect/<snippet>", redirect, name="redirect")
]