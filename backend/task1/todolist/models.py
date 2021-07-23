from django.db import models

class Todolist(models.Model):
    status = models.CharField(max_length=20)
    priority = models.CharField(max_length=20)
    duedate = models.DateTimeField()
    description = models.TextField()
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name