from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    due_time = models.DateTimeField()
    done = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)