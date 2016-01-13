from django import forms
from models import *
from wbc.projects.models import Project

class StakeholderForm(forms.ModelForm):
    class Meta:
        model = Stakeholder
        fields = '__all__'

    projects = forms.ModelMultipleChoiceField(queryset=Project.objects.all())

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self):
        instance = forms.ModelForm.save(self)
        instance.project_set.clear()
        for project in self.cleaned_data['projects']:
            instance.project_set.add(project)

        return instance

class StakeholderProfileForm(forms.ModelForm):
    class Meta:
        model = Stakeholder
        fields = ('active', 'description', 'tags', 'link',)

    # projects = forms.ModelMultipleChoiceField(queryset=Project.objects.all())

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)

    # def save(self):
    #     instance = forms.ModelForm.save(self)
    #     # instance.project_set.clear()
    #     for project in self.cleaned_data['projects']:
    #         instance.project_set.add(project)

    #     return instance