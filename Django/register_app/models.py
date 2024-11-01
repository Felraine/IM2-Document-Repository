from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Members(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    user_role = models.IntegerField()

    class Meta:
        db_table = 'members'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.fname} {self.lname}"
