from django.db import models
from Accounts.models import User
# Create your models here.

class Contact(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    message = models.TextField()
    consent = models.BooleanField()
