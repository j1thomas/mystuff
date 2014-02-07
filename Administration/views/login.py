
from . import templater
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        if user is None:
            raise forms.ValidationError("Bad username or password")
        return self.cleaned_data


def process_request(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/administration/")
                # request.user.is_authenticated()

    template_vars = {

    }
    return templater.render_to_response(request, 'login.html', {'form': form})

