from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404

from . import templater
from datetime import datetime as dt
from Administration import models as smod


def process_request(request):
    
    #get the business objects
    
    if request.urlparams[0] == 'new':
        s = smod.store()
        s.save()
        return HttpResponseRedirect('/Administration/edit_store/' + str(s.id))
    
    else:       
        s = smod.store.objects.get(id=request.urlparams[0])
    
    #Run the Form
    
    form = storesForm(initial={
        'name':s.name,
        'street':s.street,
        'city':s.city,
        'state':s.state,
        'zip_code':s.zip_code,
        'phone': s.phone,
        'schedule': s.schedule,
        'pub_date':s.pub_date,

    })
    if request.method == 'POST':
        form = storesForm(request.POST)
        if form.is_valid():
            print(">>>>>>>>>Form was VALID")
            s.name = form.cleaned_data['name']
            s.street = form.cleaned_data['address']
            s.phone = form.cleaned_data['phone']
            s.schedule = form.cleaned_data['schedule']
            s.pub_date = form.cleaned_data['pub_date']            
            s.save()
            return HttpResponseRedirect('/Administration/stores/')
            
    
    #return the template HTML
    template_vars = {
        'form': form,
    }

    return templater.render_to_response(request, 'edit_store.html', template_vars)

class storesForm(forms.Form):
    '''the stores form. imported from django up top'''
    name = forms.CharField(max_length=200)
    address = forms.CharField(max_length=200)
    phone = forms.CharField()
    schedule = forms.CharField()
    pub_date = forms.DateTimeField()
    
    
    
    
def process_request__delete(request):
    s = smod.store.objects.get(id=request.urlparams[0])
    s.active=False
    s.save()
    print("This almost deleted")
    return HttpResponseRedirect('/stores/')
    
    