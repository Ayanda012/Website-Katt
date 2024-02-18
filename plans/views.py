from datetime import date
from django.shortcuts import render
from .models import Item, Service
from .forms import QuotationForm

def quotation(request):
    if request.method == 'POST':
        form = QuotationForm(request.POST)
        if form.is_valid():
            items = form.cleaned_data['items']
            services = form.cleaned_data['services']
            today = date.today()
            total_price = sum(item.price or 0 for item in items) + sum(service.price or 0 for service in services)
            return render(request, 'plans/quotation.html', {'items': items, 'services': services, 'total_price': total_price, 'today': today, 'total_price': total_price})
    else:
        form = QuotationForm()
    return render(request, 'plans/quotation_form.html', {'form': form})