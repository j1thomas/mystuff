from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from polls import models as pmod
from . import templater



def process_request(request):
    '''shows all questions in the DB'''
    questions = pmod.Question.objects.all().order_by('question_text')
    
    
    
    template_vars = {
        'questions': questions,
        
        
    }
    
    
    return templater.render_to_response(request, 'questions.html', template_vars)