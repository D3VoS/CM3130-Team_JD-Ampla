from django.forms import ModelForm
from .models import Product
from django.contrib import messages


class ProductAddForm(ModelForm):
    class Meta:
        model = Product
        fields = ['productName', 'productPrice', 'productImageLink', 'productLink']