from django.db import models

# Create your models here.class RoomMember(models.Model):
class RoomMember(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=200)
    insession = models.BooleanField(default=True)

    class Meta:
        db_table = 'memberMeeting'

    def __str__(self):
        return self.name
    
class Attendance(models.Model):
    name = models.CharField(max_length=200)
    room_name = models.CharField(max_length=200)

    class Meta:
        db_table = 'attendance'

    def __str__(self):
        return self.name
