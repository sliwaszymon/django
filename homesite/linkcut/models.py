from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Link(models.Model):
    url = models.CharField(max_length=255, blank=False, null=False)
    snippet = models.CharField(max_length=20, blank=False, null=False, unique=True, primary_key=True)
    creation_date = models.DateTimeField("Creation date", default=timezone.now())
    visit_counter = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.snippet} | {self.url}'

    def get_absolute_url(self):
        return reverse("link-detail", kwargs={"pk": self.pk})
