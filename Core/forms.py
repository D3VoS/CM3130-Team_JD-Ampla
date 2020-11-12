from django.forms import ModelForm, Textarea
from .models import Contact
from django.utils.translation import gettext_lazy as _
class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ('title', 'message', 'consent')
        labels = {
            'title': _('Title'),
            'message': _('Message'),
            'consent': _('Consent')
        }