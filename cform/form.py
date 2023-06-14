from django import forms
from .models import CEntry


class Customer_Entry(forms.ModelForm ):
    class Meta:
        model = CEntry
        fields = '__all__'
        exclude = ['cust_id']


