from django.urls import path
from .views import TodosIndexView

urlpatterns = [
    path("", TodosIndexView.as_view(), name="todos-index"),
]
