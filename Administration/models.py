from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import AbstractUser


# Create your models here.


class store(models.Model):
    name = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    zip_code = models.CharField(max_length=9, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    schedule = models.CharField(max_length=40)
    pub_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        



class Catalog(models.Model):
    ''' Catalog of items for sale '''
    product_name = models.TextField(max_length=100)
    serial_no = models.TextField(null=True, blank=True)





class User(AbstractUser):
    '''  '''
    street = models.CharField(max_length=100, blank=True, null=True)
    street2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    postal_code = models.CharField(max_length=9, blank=True, null=True)
    country = models.CharField(max_length=25, default="U.S.A.", blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    active = models.NullBooleanField()


# class Employee(User):
#     ''' '''
#     department = models.CharField(max_length=100)
#     position = models.CharField(max_length=100)
#     salary = models.CharField()
#     hire_date = models.DateField()
#     termination_date = models.DateField()


class Catalog(models.Model):
    '''conceptual Inventory'''
    # product_ID = GUID
    title = models.CharField()
    description = models.CharField(null=True, blank=True)
    category = models.CharField()
    commission_amount = models.DecimalField(max_digits=5, decimal_places=2)
    manufacturer = models.CharField(null=True, blank=True)
    sku_number = models.CharField(null=True, blank=True)

class Inventory(models.Model):
    ''' Inventory of physical items for sale '''
    product = models.ForeignKey(Catalog)
    quantity = models.BigIntegerField(null=True)


class SaleInventory(Catalog):
    '''physical inventory'''
    catalog_item = models.ForeignKey(Catalog, related_name='catalog_sale_item')
    quantity = models.BigIntegerField()
    purchase_price = models.DecimalField(max_digits=5, decimal_places=2)
    list_price = models.DecimalField(max_digits=5, decimal_places=2)
    serial_num = models.CharField(max_length=25)
    location_ID = models.CommaSeparatedIntegerField(max_length=15)


class RentalInventory(Catalog):
    catalog_item = models.ForeignKey(Catalog, related_name='catalog_rental_item')
    # condition
    # serial_number
    # rental_rate
    # rental history (FK)


class PurchaseOrder(models.Model):
    #PO NUMBER
    purchase_date = models.DateField()
    vendor = models.CharField(max_length=50) #in a perfect world, this a FK to a Vendor list
    receive_date = models.DateField()