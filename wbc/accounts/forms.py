from django.forms import ModelForm
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm      

from .models import Profile
from .validators import validate_email_unique


class UserForm(ModelForm):
    email = forms.CharField(required=True, validators=[validate_email_unique])

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


class WbcRegistrationForm(UserCreationForm):
    email = forms.CharField(required=True, validators=[validate_email_unique])

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')        


class EmailForm(forms.Form):
    email = forms.EmailField(required=True)