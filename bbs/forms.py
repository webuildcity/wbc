from django import forms
from django.forms import ModelForm
from django.contrib.auth import authenticate, login, logout
from projects.models import Veroeffentlichung, Ort


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Benutzername und/oder Passwort ist falsch.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

class FindOrt(forms.Form):    
    orte = Ort.objects.all()
    bezeichner = forms.CharField(max_length=100, required=False)

class CreateVeroeffentlichung(ModelForm):
    class Meta:
        model = Veroeffentlichung

class CreateOrt(ModelForm):
    class Meta:
        model = Ort
        exclude = ('polygontype',)
    