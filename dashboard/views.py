from __future__ import print_function
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import InvoiceForm, InvoiceSearch, UpdateInvoice
from .models  import *
from .sms import SMS
from django.contrib import messages
#report lab imports
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY


# Dashboard contents here
def index(request):
    form = InvoiceForm(request.POST or None)
    total_invoices = Invoice.objects.count()
    queryset = Invoice.objects.order_by('-invoice_date')[:5]

    context = {
        "form": form,
        "title": "New Invoice",
        "total_invoices": total_invoices,
        "queryset": queryset,
    }
    return render(request, 'dashboard/index.html', context)

def staff(request):
    return render(request, 'dashboard/customer.html')
def product(request):
    return render(request, 'dashboard/product.html')
def orders(request):
    return render(request, 'dashboard/orders.html')

#Forms come here
def add_invoice(request):
    form = InvoiceForm(request.POST or None)
    queryset = Invoice.objects.all()
    sending = SMS()

    if form.is_valid():
        form.save()
        sending.send()
        messages.success(request, ("Invoice successfully added"))
        return redirect('/invoice_view')
    context = {
        "form": form,
        "title": "New Invoice",
    }
    return render(request, "dashboard/invoice.html", context)

#Listing invoice items
def list_invoice(request):
    title = 'All Invoices'
    queryset = Invoice.objects.all()

    form= InvoiceSearch(request.POST or None)
    context = {
        "queryset": queryset,
        "title": title,
        "form": form,
    }

    if request.method == 'POST':
        queryset = Invoice.objects.filter(invoice_no__icontains=form['invoice_no'].value(),
                                          customer_name__icontains=form['customer_name'].value())
        context = {
            "form": form,
            "queryset": queryset,
            "title": title,}

    return render(request, "dashboard/invoice_view.html", context)

#Invoice Update
def update_invoice(request, pk):
    queryset = Invoice.objects.get(id=pk)
    form = UpdateInvoice(instance=queryset)
    if request.method == 'POST':
        form = UpdateInvoice(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, ("invoice updated "))
            return redirect('/invoice_view')
    context = {
        'form':form
    }
    return render(request, 'dashboard/invoice.html', context)

#Invoice Delete
def delete_invoice(request, pk):
    queryset = Invoice.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, ("invoice deleted "))
        return redirect('/invoice_view')
    context = {
        'queryset': queryset
    }
    return render(request, 'dashboard/delete_invoice.html', context)


