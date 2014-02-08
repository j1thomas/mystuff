from django.contrib import admin

from Administration import models as smod
from Administration import models as imod
from .models import *


# Register your models here.

admin.site.register(store)
admin.site.register(Inventory)
admin.site.register(SaleInventory)
admin.site.register(RentalInventory)
admin.site.register(PurchaseOrder)
# admin.site.register(User, UserAdmin)
