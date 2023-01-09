from django.urls import path
from . import views

urlpatterns = [
   path('', views.homepage),
   path('task', views.task, name="task")
]