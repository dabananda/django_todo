from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    status = models.BooleanField(default=False)