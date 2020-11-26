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
        'eventDescription',
        'eventLocation',
        'eventDate', 
        'eventStart', 
        'eventEnd',
        'eventCapacity', 
        'eventCost'
        ]

        labels = {
        'eventName': 'Event Name', 
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
            'eventName' : TextInput(attrs={'placeholder' : 'Swimming with Hannah! (Beginners)'}),
            'eventDate' : DateInput(format = ['%d/%m/%Y'], attrs={'type': 'date'}),
            'eventLocation' : TextInput(attrs={'placeholder': 'Robert Gordon University Gym Hall 3'}),
            'eventStart' : TimeInput(attrs={'type': 'time'}),
            'eventEnd' : TimeInput(attrs={'type': 'time'}),
            'eventDescription' : Textarea(attrs={'placeholder':'Join me for an hour swim session where I will be teaching beginners the basics of swimming!'}),
            'eventCapacity' : NumberInput(attrs={'placeholder':'The total Capacity of the sessiom, e.g. 30'}),
            'eventCost' : NumberInput(attrs={'placeholder': 'Cost in Pounds: £30 = 30'})
        }