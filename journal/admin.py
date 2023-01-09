from django.contrib import admin

# Register your models here.
from .models import Task, Review

admin.site.register(Task)
admin.site.register(Review)
