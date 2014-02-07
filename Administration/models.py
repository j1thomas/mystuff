from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib import admin

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

class UserAdmin(admin.ModelAdmin):
    pass
        
class User(AbstractBaseUser):
    '''  '''
    username = models.CharField(max_length=30, unique=True, default='username')
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField()
    street = models.CharField(max_length=100, blank=True, null=True)
    street2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    postal_code = models.CharField(max_length=9, blank=True, null=True)
    country = models.CharField(max_length=25, default="U.S.A.", blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    active = models.BooleanField(default=True)






    USERNAME_FIELD = 'username'


# class Employee(User):
#     ''' '''
#     department = models.CharField(max_length=100)
#     position = models.CharField(max_length=100)
#     salary = models.CharField()
#     hire_date = models.DateField()
#     termination_date = models.DateField()


class Inventory(models.Model):
    '''conceptual Inventory'''
    # product_ID = GUID
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=225, null=True, blank=True)
    category = models.CharField(max_length=25)
    commission_amount = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    manufacturer = models.CharField(max_length=25,null=True, blank=True)
    sku_number = models.CharField(max_length=25, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return '%s : %s' % (self.id, self.title)



class SaleInventory(Inventory):
    '''physical inventory'''
    quantity = models.BigIntegerField(null=True)
    purchase_price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    list_price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    serial_num = models.CharField(max_length=25, null=True)
    location_ID = models.CommaSeparatedIntegerField(max_length=15, null=True)


class RentalInventory(Inventory):
    condition = models.CharField(max_length=25, null=True, blank=True)
    serial_number = models.CharField(max_length=25, null=True, blank=True)
    rental_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    rental_history = models.CharField(max_length=25, null=True, blank=True)



class PurchaseOrder(models.Model):
    #PO NUMBER
    purchase_date = models.DateField()
    vendor = models.CharField(max_length=50) #in a perfect world, this a FK to a Vendor list
    receive_date = models.DateField()