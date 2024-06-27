from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('Mobile Phone', 'Mobile Phone'),
    ('Audio Devices', 'Audio Devices'),
    ('TV', 'TV'),
    ('Accessories', 'Accessories'),
)
# class


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.name}-{self.quantity}'

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    order_quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'

class Invoice(models.Model):
    #Main Details
    comments = models.TextField(max_length= 3000, default='', blank=True, null=True)
    invoice_no = models.IntegerField(null=True, blank=True)
    invoice_date=models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    customer_name=models.CharField('Customer Name', max_length=120, default='', blank=True, null=True)

    #Entries #1
    fe= models.CharField('First Entry', max_length=120, default='', blank=True, null=True)
    fe_quantity= models.IntegerField('Quantity', max_length=120, default=0, blank=True, null=True)
    fe_unit_price= models.IntegerField('Unit Price', max_length=120, default=0, blank=True, null=True)
    fe_totals= models.IntegerField('Totals', max_length=120, default=0, blank=True, null=True)
     #Entries #2
    se= models.CharField('Second Entry', max_length=120, default='', blank=True, null=True)
    se_quantity= models.IntegerField('Quantity', max_length=120, default=0, blank=True, null=True)
    se_unit_price= models.IntegerField('Unit Price', max_length=120, default=0, blank=True, null=True)
    se_totals= models.IntegerField('Totals', max_length=120, default=0, blank=True, null=True)
    #Entries #3
    te= models.CharField('Third Entry', max_length=120, default='', blank=True, null=True)
    te_quantity= models.IntegerField('Quantity', max_length=120, default=0, blank=True, null=True)
    te_unit_price= models.IntegerField('Unit Price', max_length=120, default=0, blank=True, null=True)
    te_totals= models.IntegerField('Totals', max_length=120, default=0, blank=True, null=True)
    #Entries #4
    fte= models.CharField('Fourth Entry', max_length=120, default='', blank=True, null=True)
    fte_quantity= models.IntegerField('Quantity', max_length=120, default=0, blank=True, null=True)
    fte_unit_price= models.IntegerField('Unit Price', max_length=120, default=0, blank=True, null=True)
    fte_totals= models.IntegerField('Totals', max_length=120, default=0, blank=True, null=True)
    #Entries #5
    ffe= models.CharField('Fifth Entry', max_length=120, default='', blank=True, null=True)
    ffe_quantity= models.IntegerField('Quantity', max_length=120, default=0, blank=True, null=True)
    ffe_unit_price= models.IntegerField('Unit Price', max_length=120, default=0, blank=True, null=True)
    ffe_totals= models.IntegerField('Totals', max_length=120, default=0, blank=True, null=True)

    #Details
    contact = models.CharField(max_length=120, default='', blank=True, null=True)
    total = models.IntegerField(default=0,  blank=True, null=True)
    balance = models.IntegerField(default=0,  blank=True, null=True)
    time =models.DateTimeField(auto_now_add=True, auto_now=False)
    last_update = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True)
    paid=models.BooleanField(default=False)

    #selection
    inv_type= (
        ('Receipt', 'Receipt'),
        ('Invoice', 'Invoice'),
        ('Debit Note', 'Debit Note'),
        ('Credit Note', 'Credit Note')
    )

    inv_selection = models.CharField(max_length=120, default = '', blank=True, null=True,
                                     choices=inv_type)

    def __unicode__(self):
        return self.invoice_no

    #return the customer name as the invoice name
    def __str__(self):
        return (str(self.customer_name))
