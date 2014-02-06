from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from Administration import models as smod
from . import templater
from datetime import datetime as dt
from Administration import models as imod


def process_request(request):

    #get the business objects

    if request.urlparams[0] == 'new':
        i = imod.SaleInventory
        i.save()
        return HttpResponseRedirect('/Administration/edit_sale_inventory/' + str(i.id))

    else:
        i = imod.SaleInventory.objects.get(id=request.urlparams[0])

    #Run the Form

    form = inventoryForm(initial={
        'title':i.title,
        'description':i.description,
        'category':i.category,
        'commission_amount':i.commission_amount,
        'sku number':i.sku_number,

    })
    if request.method == 'POST':
        form = inventoryForm(request.POST)
        if form.is_valid():
            print(">>>>>>>>>Form was VALID")
            i.title = form.cleaned_data['title']
            i.description = form.cleaned_data['description']
            i.category = form.cleaned_data['category']
            i.commission_amount = form.cleaned_data['commission_amount']
            i.sku_number = form.cleaned_data['sku_number']
            i.save()
            return HttpResponseRedirect('/Administration/')


    #return the template HTML
    template_vars = {
        'form': form,
    }

    return templater.render_to_response(request, 'edit_inventory.html', template_vars)

class inventoryForm(forms.Form):
    '''the stores form. imported from django up top'''
    title = forms.CharField(max_length=200)
    description = forms.CharField(max_length=200)
    category = forms.CharField()
    commission_amount = forms.CharField()
    sku_number = forms.CharField()




def process_request__delete(request):
    i = imod.store.objects.get(id=request.urlparams[0])
    i.active=False
    i.save()
    print("This almost deleted")
    return HttpResponseRedirect('/Administration/sale_inventory/')

