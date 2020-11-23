from django.forms import ModelForm, Textarea
from .models import Contact
from django.utils.translation import gettext_lazy as _
class ContactForm(ModelForm):
    def __init__(self, *args, **kwargs):
            #Allows an extra paramater to be passed and captured
            self.creator = kwargs.pop('creator', None)
            #Continues the original __init__
            super(ContactForm, self).__init__(*args,**kwargs)
        #Overrides the ModelForm save 
    def save(self, commit=True):
        obj = super(ContactForm, self).save(commit=False)
        #Adds the user to the form after it has been submitted
        obj.creator = self.creator
        if commit:
            #Saves the object to the database
            obj.save()
        return obj

    class Meta:
        model = Contact
        fields = ('title', 'message')
        labels = {
            'title': _('Title'),
            'message': _('Message')
        }