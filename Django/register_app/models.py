from django.db import models

class Members(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=128)


    def __str__(self):
        return self.fname
