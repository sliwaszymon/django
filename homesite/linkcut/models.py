from django.db import models
from datetime import datetime

# Create your models here.
class Link(models.Model):
    url = models.CharField(max_length=255, blank=False, null=False)
    snippet = models.CharField(max_length=20, blank=False, null=False, unique=True, primary_key=True)
    creation_date = models.DateTimeField("Creation date", default=datetime.now())
    visit_counter = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.snippet} | {self.link}'
    
