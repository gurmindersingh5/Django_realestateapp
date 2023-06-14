from django.shortcuts import render, redirect
from cform.models import CEntry
from inventory.models import PEntry
from eform.models import DEntry
from .form import DataEntry
from django.urls import reverse
import datetime
from django.http import JsonResponse




LASTENTRY = {'Name': '', 'Address': '', 'Parts_purchased': '',
             'date': '', 'time': ''}
error_note = ""


def e_form(request):
    form_data = DataEntry(request.POST)
    data_list = CEntry.objects.all()
    part_list = PEntry.objects.all()
    address_list = {}
    parts = {}
    global error_note

    for item in data_list:
        address_list[item.name] = item.address
    for part in part_list:
        parts[part.name] = float(part.price)
    
 

    if request.GET.get('Parts_purchased') and request.GET.get('custid') and request.GET.get('Price') and request.GET.get('qty'):
        try:
            print(request.GET.get('Parts_purchased'), request.GET.get('custid') , request.GET.get('Price') , request.GET.get('qty'))
            parts_purchased = request.GET.get('Parts_purchased')
            qty = request.GET.get('qty')
            price = request.GET.get('Price')
            cust_id = request.GET.get('custid')
            # fix = CEntry.objects.get(cust_id=cust_id)
            c_entry = CEntry.objects.get(cust_id=cust_id)

            print('\n'*5)
            print(c_entry)
            print(request.GET.get('Parts_purchased') and request.GET.get('custid') and request.GET.get('Price') and request.GET.get('qty'))
            print(cust_id,parts,qty,price)
            print('\n'*5)



            DEntry_data = DEntry(
                parts=parts_purchased,
                qty=qty,
                price=price,
                time=datetime.datetime.now(),
                cust_id=c_entry
            ) 
            DEntry_data.save()
            error_note = "Saved into database"
        except:
            error_note = "Please complete all fields"
        finally:
            return redirect(reverse('e_form'))


 
    if request.method == "POST":

        selected_part = request.POST.get('part')
        price = parts[selected_part]
        return JsonResponse({'intendedPrice': price})


    if request.method == "POST":
        global LASTENTRY
        error_note = ""
        if form_data.is_valid():
            form_data.save()
            selected_customer = CEntry.objects.filter(cust_id=request.POST.get('custid')).first()
            LASTENTRY['Name'] = selected_customer.name
            LASTENTRY['Address'] = selected_customer.name
            LASTENTRY['Name'] = selected_customer.name
            LASTENTRY['Name'] = selected_customer.name

            inv = PEntry.query.filter_by(name=request.POST.get('Parts_purchased')).first()
            if inv.qty - form_data.Qty.data >= 0:
                inv.qty = inv.qty - form_data.Qty.data
                form_data.save()
                LASTENTRY['Name'] = selected_customer
            else:
                error_note = f"Not enough Inventory. Available qty: {inv.qty}"

           
            return redirect(reverse('e_form'))
        if form_data.errors != {}:
            for err_msg in form_data.errors.values():
                print(f" There was an error {err_msg, form_data.errors}")

    return render(request, 'eform/eform.html', {'form':form_data, 'name_list':address_list.items(), 'part_list':parts,
                           'address_list':address_list,
                           'lastentry':LASTENTRY, 'error_note':error_note})

