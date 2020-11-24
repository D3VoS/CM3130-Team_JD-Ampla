from django.db import models
from Accounts.models import User
# Create your models here.

class event(models.Model):
    eventCreator = models.ForeignKey(User, on_delete=models.CASCADE)
    eventName = models.CharField(max_length=50)
    eventDate = models.DateField()
    eventLocation = models.CharField(max_length=50)
    eventStart = models.TimeField()
    eventEnd = models.TimeField()
    eventDescription = models.CharField(max_length=1000)
    eventCapacity = models.IntegerField()
    eventCost = models.FloatField(max_length=6)
    eventBooked = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.eventCreator} { self.eventDate}'

class bookingEvent(models.Model):
    bookingEventID = models.ForeignKey(event, on_delete=models.CASCADE)
    bookingUser = models.ForeignKey(User, on_delete=models.CASCADE)
