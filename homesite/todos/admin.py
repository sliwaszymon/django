from django.contrib import admin
from .models import Section, Todo, Board

# Register your models here.
admin.site.register(Todo)
admin.site.register(Section)
admin.site.register(Board)