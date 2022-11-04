from django.db import models

# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=30)
    taskDesc = models.TextField()
    time=models.DateTimeField(auto_now_add=True)   #shows current time

    def __str__(self):
        return self.taskTitle   #displays only the task title
