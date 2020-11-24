from django import forms
from Calendar.models import event

class createSession(forms.ModelForm):
    class Meta:
        model = event
        fields = ['eventName', 'eventDate', 'eventLocation', 'eventStart', 'eventEnd',
        'eventDescription', 'eventCapacity', 'eventCost']
        