from django.shortcuts import render
from django.http import HttpResponse
from . models import Task

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def task(request):
    queryAllData = Task.objects.get(title="Going to movies")

    context = {'task': queryAllData}



    return render(request, 'task.html', context)