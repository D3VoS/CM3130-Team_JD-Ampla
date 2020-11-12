from django.db import models
from Accounts.models import User
# Create your models here.

class myCalendar(models.Model):
    myCreator = models.ForeignKey(User, on_delete=models.CASCADE)
    myName = models.CharField(max_length=50)
    myDate = models.DateField()
    myLocation = models.CharField(max_length=50)
    myDuration = models.IntegerField()
    myDescription = models.CharField(max_length=1000)
    myCapacity = models.IntegerField()
    myCost = models.FloatField(max_length=6)
    myBooked = models.IntegerField()

#class CreateEvent(models.Model):
    #eventCreator = models.CharField()