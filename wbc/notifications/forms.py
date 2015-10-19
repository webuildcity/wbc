# -*- coding: utf-8 -*-
from django import forms

class SubscribeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        if 'entities' in kwargs:
            entities = kwargs.pop('entities')

        kwargs['label_suffix'] = ''
        super(SubscribeForm, self).__init__(*args, **kwargs)

        for entity in entities:
            field = forms.BooleanField(label=entity['name'],required=False);
            self.fields[str(entity['id'])] = field

        self.fields['email'] = forms.EmailField(label='Email',
                                                widget=forms.TextInput(attrs={'class':'form-control'}))

class UnsubscribeForm(forms.Form):
    email = forms.EmailField(label='Email-Adresse',
                             widget=forms.TextInput(attrs={'class':'form-control'}))
