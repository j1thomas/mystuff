from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from Administration import models as imod
from . import templater


def process_request(request):
    inventory = imod.SaleInventory.objects.exclude(active=False)


    template_vars = {
        'inventory': inventory,
    }

    return templater.render_to_response(request, 'inventory.html', template_vars)

