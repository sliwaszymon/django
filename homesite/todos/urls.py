from django.urls import path

from .views import TodosView, TodoDeleteView, TodoUpdateView, SectionDeleteView, BoardsView, BoardDeleteView

urlpatterns = [
    path("", BoardsView.as_view(), name="todos-index"),
    path("board/<pk>/", TodosView.as_view(), name="board"),
    path("board/<pk>/delete/", BoardDeleteView.as_view(), name="board-delete"),
    path("board/<board_pk>/todo/<pk>/delete/", TodoDeleteView.as_view(), name="todo-delete"),
    path("board/<board_pk>/todo/<pk>/update/", TodoUpdateView.as_view(), name="todo-update"),
    path("board/<board_pk>/section/<pk>/delete/", SectionDeleteView.as_view(), name="section-delete")
]
