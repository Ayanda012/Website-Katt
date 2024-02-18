# forms.py
from django import forms
from .models import Item, Service

from django import forms
from .models import Item, Service

class QuotationForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(max_length=100, label="Your Email")
    phone_number = forms.CharField(max_length=20, label="Your Phone Number")
    address = forms.CharField(max_length=200, label="Your Address")
    items = forms.ModelMultipleChoiceField(queryset=Item.objects.all(), widget=forms.CheckboxSelectMultiple)
    services = forms.ModelMultipleChoiceField(queryset=Service.objects.all(), widget=forms.CheckboxSelectMultiple)
