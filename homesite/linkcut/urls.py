from django.urls import path
from .views import IndexView, CutItFormView #, LinkDetailView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("cutit", CutItFormView.as_view(), name="cutit"),
    # path("link/<pk>", LinkDetailView.as_view(), name="link-detal")
]