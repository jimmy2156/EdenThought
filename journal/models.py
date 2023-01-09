from django.db import models

# Create your models here.
class Task(models.Model):
    

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)

class Review(models.Model):


    reviewer_name = models.CharField(max_length=65)
    review_title = models.CharField(max_length=100)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
