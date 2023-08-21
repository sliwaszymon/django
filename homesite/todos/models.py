from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Board(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    owner = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='boards')
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    todo_cap = models.IntegerField(default=0)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='sections')

    def __str__(self):
        return self.name


class Todo(models.Model):
    section = models.ForeignKey(Section, null=True, on_delete=models.SET_NULL, related_name='todos')
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='todos')
    description = models.CharField(max_length=255, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField("Deadline date", default=timezone.now() + timezone.timedelta(days=7))
    color = models.CharField(max_length=7, default="#6495ED")

    def __str__(self):
        return self.description
