from django.urls import path
from .views import TodosIndexView, TodoDeleteView, TodoUpdateView, SectionDeleteView

urlpatterns = [
    path("", TodosIndexView.as_view(), name="todos-index"),
    path("todo/<pk>/delete/", TodoDeleteView.as_view(), name="todo-delete"),
    path("todo/<pk>/update/", TodoUpdateView.as_view(), name="todo-update"),
    path("section/<pk>/delete/", SectionDeleteView.as_view(), name="section-delete")
]
