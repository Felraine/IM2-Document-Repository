from django.db import models

class Members(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    user_role = models.IntegerField()

    class Meta:
        db_table = 'members'

    def __str__(self):
        return f"{self.fname} {self.lname}"
