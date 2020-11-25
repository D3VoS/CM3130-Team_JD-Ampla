from django import forms
from .models import event

class createSession(forms.ModelForm):
    class Meta:
        model = event
        fields = ['eventCreator', 'eventName', 'eventDate', 'eventLocation', 'eventStart', 'eventEnd',
        'eventDescription', 'eventCapacity', 'eventCost']
        