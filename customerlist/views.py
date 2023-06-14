from django.shortcuts import render, redirect
from cform.models import CEntry
from django.db import models as db
from eform.models import DEntry
from .form import search_form
import datetime
from django.urls import reverse



# Create your views here.
def customerlist(request, cust_id=None):
    query = CEntry.objects.all()
    results = query.order_by('name').all()

    form_data = search_form(request.POST)
    NOTE = ""

    if request.GET.get('sort'):
        if request.GET.get('sort') == 'name':
            items = query.order_by('-name').all()
            return redirect(reverse('customerlist'))
        else:
            slug_id = request.GET.get('sort')
            t = 0
            total = ""
            customer_data = CEntry.objects.filter(cust_id=slug_id).first()
            customer_purchased_data = DEntry.objects.filter(cust_id=slug_id)
            for item in customer_purchased_data:
                t += item.price
            c = 0
            l = len(str(int(t)))
            for item in reversed(str(int(t))):
                c += 1
                total += item
                l -= 1
                if c == 3 and l > 0:
                    total += ","
                    c = 0
            return render(request, 'customerlist/customerdata.html', {'customer_data':customer_data,
                                   'customer_purchased_data':customer_purchased_data.all(), 'total':total[::-1]})

    if request.method == "POST":
        results = []
        if form_data.data['S_name']:
            results = query.filter(name__icontains=form_data.data['S_name'])
        if form_data.data['S_address']:
            results = query.filter(address__icontains=form_data.data['S_address'])

    if not results:
        NOTE = "Not found in database"
    else:
        NOTE = f"{len(results)} entry/ies"

    return render(request, 'customerlist/customerlist.html', {'form':form_data, 'results':results, 'note':NOTE})
