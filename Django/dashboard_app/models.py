from django.db import models

#Adding Events
class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    location = models.CharField(max_length=100)
    dateTime = models.DateTimeField()

    class Meta:
        db_table = 'events'
    
    def __str__(self):
        return self.title

class Task(models.Model):
    dateAssigned = models.DateField()
    taskTitle  = models.CharField(max_length=50)
    taskDescription = models.TextField(max_length=255)
    dueDate = models.DateTimeField()
    assignTo = models.ForeignKey('register_app.Members', on_delete=models.CASCADE, null=True)
    
    class Meta:
        db_table = 'tasks'
        
    def __str__(self):
        return self.taskTitle

    


