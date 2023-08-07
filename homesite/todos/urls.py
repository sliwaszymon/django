from django.urls import path
from .views import TodosIndexView, TodoDeleteView

urlpatterns = [
    path("", TodosIndexView.as_view(), name="todos-index"),
    path("todo/<pk>/delete/", TodoDeleteView.as_view(), name="todo-delete")
]
