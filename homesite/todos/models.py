from django.db import models
from django.utils import timezone


class Section(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    todo_cap = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Todo(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=False, null=False)
    deadline = models.DateTimeField("Deadline date", default=timezone.now() + timezone.timedelta(days=7))
    color = models.CharField(max_length=7, default="#6495ED")

    def __str__(self):
        return self.description

