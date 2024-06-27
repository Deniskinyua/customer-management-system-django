from django.contrib import admin
from .models import Product, Order, Invoice
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .forms import InvoiceForm

# Register your models here.
admin.site.site_header = 'Customer Management System'
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')
    list_filter = ('category',)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
# admin.site.unregister(Group)

#Invoice
#class
class InvoiceTable(admin.ModelAdmin):
    list_display = ('invoice_no', 'customer_name', 'contact', 'invoice_date',)
    form = InvoiceForm
    list_filter = ('customer_name',)
    search_fields = ('customer_name', 'invoice_no',)

admin.site.register(Invoice, InvoiceTable)
