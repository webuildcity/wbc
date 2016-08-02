from django.forms import ModelForm
from django import forms

from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm      

from .models import Profile
from .validators import validate_email_unique, validate_email_unique_change, validate_username_unique


class UserForm(ModelForm):
    email = forms.EmailField(required=True)

    def clean_email(self):
        print self.user
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email=email).exists() and User.objects.get(email=email) != self.user:
            raise ValidationError("E-Mail-Adresse wird bereits verwendet.")
        return email

    def __init__(self, *args, **kwargs):
         self.user = kwargs.pop('user',None)
         super(UserForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


class WbcRegistrationForm(UserCreationForm):
    username = forms.CharField(required=True, validators=[validate_username_unique])
    email = forms.EmailField(required=True)


    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email=email).exists():
            raise ValidationError("E-Mail-Adresse wird bereits verwendet.")
        return email

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')        


class EmailForm(forms.Form):
    email = forms.EmailField(required=True)