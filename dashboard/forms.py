from django import forms
from .models import Invoice


#Populate invoice form
class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['customer_name', 'contact','invoice_no', 'invoice_date',
                  'fe', 'fe_quantity', 'fe_unit_price', 'fe_totals',
                   'se', 'se_quantity', 'se_unit_price', 'se_totals',
                   'te', 'te_quantity', 'te_unit_price', 'te_totals',
                   'fte', 'fte_quantity', 'fte_unit_price', 'fte_totals',
                   'ffe', 'ffe_quantity', 'ffe_unit_price', 'ffe_totals',
                  'total', 'paid', 'inv_selection',
                  ]
    def clean_invoice_no(self):
        invoice_no = self.cleaned_data.get('invoice_no')
        if not invoice_no:
            raise forms.ValidationError('Invoice number is required')
        return invoice_no

    def clean_customer_name(self):
        customer_name = self.cleaned_data.get('customer_name')
        if not customer_name:
            raise forms.ValidationError('Customer name is required')
        return customer_name

    def clean_contact(self):
        contact = self.cleaned_data.get('contact')
        if not contact:
            raise forms.ValidationError('Customer contact is required')
        return contact

    def clean_fe(self):
        fe = self.cleaned_data.get('fe')
        if not fe:
            raise forms.ValidationError('Item entry is required')
        return fe


# Form Search
class InvoiceSearch(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_no', 'customer_name']

#Update Invoice
class UpdateInvoice(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['customer_name', 'contact','invoice_no', 'invoice_date',
                  'fe', 'fe_quantity', 'fe_unit_price', 'fe_totals',
                   'se', 'se_quantity', 'se_unit_price', 'se_totals',
                   'te', 'te_quantity', 'te_unit_price', 'te_totals',
                   'fte', 'fte_quantity', 'fte_unit_price', 'fte_totals',
                   'ffe', 'ffe_quantity', 'ffe_unit_price', 'ffe_totals',
                  'total', 'paid', 'inv_selection',
                  ]
    def clean_invoice_no(self):
        invoice_no = self.cleaned_data.get('invoice_no')
        if not invoice_no:
            raise forms.ValidationError('Invoice number is required')
        return invoice_no

    def clean_customer_name(self):
        customer_name = self.cleaned_data.get('customer_name')
        if not customer_name:
            raise forms.ValidationError('Customer name is required')
        return customer_name

    def clean_contact(self):
        contact = self.cleaned_data.get('contact')
        if not contact:
            raise forms.ValidationError('Customer contact is required')
        return contact

    def clean_fe(self):
        fe = self.cleaned_data.get('fe')
        if not fe:
            raise forms.ValidationError('Item entry is required')
        return fe
