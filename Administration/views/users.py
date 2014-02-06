from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from Administration import models as umod
from . import templater


def process_request(request):
    user = umod.User.objects.exclude(active=False)


    template_vars = {
        'User': user,
    }

    return templater.render_to_response(request, 'users.html', template_vars)

