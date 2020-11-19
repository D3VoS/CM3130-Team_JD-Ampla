from django.forms import ModelForm
from .models import Product
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class ProductAddForm(ModelForm):
    class Meta:
        model = Product
        fields = ['productName', 'productPrice', 'productImageLink', 'productLink']
        labels = {
            'productName': _('Name'),
            'productPrice': _('Price'),
            'productImageLink': _('Link To Image'),
            'productLink': _('Link To Product')
        }