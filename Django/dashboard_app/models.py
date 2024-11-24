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

