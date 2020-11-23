from django.db import models
from Accounts.models import User
# Create your models here.

class Contact(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    message = models.TextField()
    consent = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.title
    
    @property
    def is_active(self):
        return self.active
