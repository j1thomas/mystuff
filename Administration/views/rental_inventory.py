from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from Administration import models as imod
from . import templater


def process_request(request):
    Rental_Inventory = imod.RentalInventory.objects.exclude(active=False)


    template_vars = {
        'rental_inventory': Rental_Inventory,
    }

    return templater.render_to_response(request, 'rental_inventory.html', template_vars)

