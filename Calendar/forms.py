from django import forms
from django.forms.fields import DateField
from django.forms.widgets import DateInput, HiddenInput, NumberInput, TextInput, Textarea, TimeInput
from .models import bookingEvent, event

class createSession(forms.ModelForm):
    class Meta:
        model = event

        fields = [
        'eventCreator',
        'eventName', 
        'eventDate', 
        'eventLocation', 
        'eventStart', 
        'eventEnd',
        'eventDescription', 
        'eventCapacity', 
        'eventCost'
        ]

        labels = {
        'eventName': 'Name', 
        'eventDate': 'Date', 
        'eventLocation': 'Location', 
        'eventStart': 'Starting Time', 
        'eventEnd': 'Finishing Time',
        'eventDescription': 'Description', 
        'eventCapacity': 'Capacity', 
        'eventCost': 'Cost'
        }

        widgets = {
            'eventCreator' : HiddenInput,
            'eventName' : TextInput,
            'eventDate' : DateInput(format = ['%d/%m/%Y'], attrs={'type': 'date'}),
            'eventLocation' : TextInput,
            'eventStart' : TimeInput(attrs={'type': 'time'}),
            'eventEnd' : TimeInput(attrs={'type': 'time'}),
            'eventDescription' : Textarea,
            'eventCapacity' : NumberInput,
            'eventCost' : NumberInput
        }