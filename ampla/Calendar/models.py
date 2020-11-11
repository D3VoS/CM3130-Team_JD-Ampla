from django.db import models
from ampla.Accounts import models as accountModels
# Create your models here.

class myCalendar(models.Model):
    myCreator = models.ForeignKey(accountModels.email, on_delete=models.CASCADE)
    myName = models.CharField(max_length=50)
    myDate = models.DateField()
    myLocation = models.CharField(max_length=50)
    myDuration = models.IntegerField(max_length=4)
    myDescription = models.CharField(max_length=1000)
    myCapacity = models.IntegerField(max_length=4)
    myCost = models.FloatField(max_length=6)
    myBooked = models.IntegerField(max_length=4)

#class CreateEvent(models.Model):
    #eventCreator = models.CharField()