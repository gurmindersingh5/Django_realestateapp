from django.shortcuts import render, redirect
from cform.models import CEntry
from .form import Customer_Entry
from django.urls import reverse

success_note = ""


def c_form(request):
    global success_note
    form_data = Customer_Entry(request.POST)

    if form_data.is_valid():
        print(form_data.is_valid()*100)
        form_data.save()
        success_note = f"Success: Customer - {form_data.data['name']}, {form_data.data['address']}, {form_data.data['contact']} was created."
        return redirect(reverse('c_form'))
    if form_data.errors != {}:
        for err_msg in form_data.errors.values():
            print(f" There was an error {err_msg}")

    return render(request, 'cform/cform.html', {'form':form_data, 'success_note':success_note})
