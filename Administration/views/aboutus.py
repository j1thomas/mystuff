from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from calculator.models import *
from . import templater


################################################################
###   Main calculator page functionality

def process_request(request):
  return templater.render_to_response(request, 'trial.html')
