from django import forms
from .models import DEntry

class DataEntry(forms.ModelForm):
    class Meta:
        model = DEntry
        fields = '__all__'
        exclude = ['cust_id']

