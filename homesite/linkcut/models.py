from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Link(models.Model):
    url = models.CharField(max_length=255, blank=False, null=False)
    snippet = models.CharField(max_length=20, blank=False, null=False, unique=True, primary_key=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='links', null=True)
    creation_date = models.DateTimeField("Creation date", auto_now_add=True)
    last_visit_date = models.DateTimeField(auto_now=True)
    visit_counter = models.IntegerField(default=0)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.snippet} | {self.url}'

    def get_absolute_url(self):
        return reverse("link-detail", kwargs={"pk": self.pk})
