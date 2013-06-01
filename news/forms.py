from django import forms

class AbonierenForm(forms.Form):
    def __init__(self, *args, **kwargs):
        if (kwargs.has_key('bezirke')):
            bezirke = kwargs.pop('bezirke')

        super(AbonierenForm, self).__init__(*args, **kwargs)

        for bezirk in bezirke:
            field = forms.BooleanField(label=bezirk['name'],required=False);
            self.fields[str(bezirk['id'])] = field

        field = forms.EmailField(label='Email-Adresse')
        field.widget.attrs.update({
            'class': 'input-xlarge'
        })
        self.fields['email'] = field

class AbbestellenForm(forms.Form):
    email = forms.EmailField(label='Email-Adresse')
    email.widget.attrs.update({
        'class': 'input-xlarge'
    })


        

