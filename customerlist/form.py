from django import forms

class search_form(forms.Form):
    S_name = forms.CharField(max_length=100, label='Search by Name: ', required=False)
    S_address = forms.CharField(max_length=200, label='Search by Address: ', required=False)

