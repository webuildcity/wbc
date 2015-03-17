# -*- coding: utf-8 -*-
from django import forms

class AbonnierenForm(forms.Form):
    def __init__(self, *args, **kwargs):
        if (kwargs.has_key('bezirke')):
            bezirke = kwargs.pop('bezirke')

        kwargs['label_suffix'] = ''
        super(AbonnierenForm, self).__init__(*args, **kwargs)

        for bezirk in bezirke:
            field = forms.BooleanField(label=bezirk['name'],required=False);
            self.fields[str(bezirk['id'])] = field

        self.fields['email'] = forms.EmailField(label='Email',
                                                widget=forms.TextInput(attrs={'class':'form-control'}))

class AbbestellenForm(forms.Form):
    email = forms.EmailField(label='Email-Adresse',
                             widget=forms.TextInput(attrs={'class':'form-control'}))
