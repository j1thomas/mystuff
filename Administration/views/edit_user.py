from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404

from . import templater
from datetime import datetime as dt
from Administration import models as umod


def process_request(request):

    #get the business objects

    if request.urlparams[0] == 'new':
        u = umod.User()
        u.save()
        return HttpResponseRedirect('/Administration/edit_user/' + str(u.id))

    else:
        u = umod.User.objects.get(id=request.urlparams[0])

    #Run the Form

    form = UserForm(initial={
        'username':u.username,
        'first_name':u.first_name,
        'last_name':u.last_name,
        'email':u.email,
        'password':u.password,
        'street': u.street,
        'street2': u.street2,
        'city': u.city,
        'postal_code': u.postal_code,
        'country': u.country,
        'phone': u.phone,

    })
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print(">>>>>>>>>Form was VALID")
            u.username = form.cleaned_data['username']
            u.first_name = form.cleaned_data['first_name']
            u.last_name = form.cleaned_data['last_name']
            u.email = form.cleaned_data['email']
            u.password = form.password
            u.street = form.cleaned_data['street']
            u.street2 = form.cleaned_data['street2']
            u.city = form.cleaned_data['city']
            u.state = form.cleaned_data['state']
            u.postal_code = form.cleaned_data['postal_code']
            u.country = form.cleaned_data['country']
            u.phone = form.cleaned_data['phone']


            u.save()
            return HttpResponseRedirect('/Administration/users/')


    #return the template HTML
    template_vars = {
        'form': form,
    }

    return templater.render_to_response(request, 'edit_user.html', template_vars)

class UserForm(forms.Form):
    '''the stores form. imported from django up top'''
    username = forms.CharField(max_length=200)
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.PasswordInput
    street = forms.CharField(max_length=100)
    street2 = forms.CharField(max_length=100)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=20)
    postal_code = forms.IntegerField(max_value=99999)
    country = forms.CharField(max_length=25)
    phone = forms.CharField(max_length=15)






def process_request__delete(request):
    u = umod.User.objects.get(id=request.urlparams[0])
    u.active=False
    u.save()
    print("This almost deleted")
    return HttpResponseRedirect('/users/')

