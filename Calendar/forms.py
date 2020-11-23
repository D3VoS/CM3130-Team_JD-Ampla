from django import forms
from Calendar.models import event



class createSession(forms.ModelForm):
    class Meta:
        model = event
        exclude = ['eventCreator', 'eventBooked']
        


form = createSession