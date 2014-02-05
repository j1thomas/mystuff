from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from Administration import models as smod
from . import templater


def process_request(request):
    stores = smod.store.objects.exclude(active=False)
    
    
    template_vars = {
        'stores': stores,
    }

    return templater.render_to_response(request, 'stores.html', template_vars)

