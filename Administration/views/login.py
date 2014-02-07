from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from Administration import models as smod
from . import templater
from django.contrib.auth import authenticate, login


def process_request(request):
    form = LoginForm()

    if request.method == "POST":
        print("I hit the sserver!")
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user!= None:
                login(request,user)
                return HttpResponseRedirect('/Administration')

                request.user.is_authenticated()

    return templater.render_to_response(request, 'login.html', {'form':form})


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    def clean(self):
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        if user==None:
            raise forms.ValidationError('Bad Username or Password')

        return self.cleaned_data