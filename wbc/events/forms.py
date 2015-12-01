from django import forms
from models import *
from wbc.projects.models import Project

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

    projects = forms.ModelMultipleChoiceField(queryset=Project.objects.all())

    def __init__(self, *args, **kwargs):
    # Only in case we build the form from an instance
    # (otherwise, 'toppings' list should be empty)
        # print kwargs
        # if 'instance' != None:
        #     # We get the 'initial' keyword argument or initialize it
        #     # as a dict if it didn't exist.                
        #     initial = kwargs.setdefault('initial', {})
        #     # The widget for a ModelMultipleChoiceField expects
        #     # a list of primary key for the selected data.
        #     initial['projects'] = [t.pk for t in kwargs['instance'].project_set.all()]

        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self):
        instance = forms.ModelForm.save(self)
        instance.projects_events.clear()
        for project in self.cleaned_data['projects']:
            instance.projects_events.add(project)

        return instance

class DateForm(EventForm):
    class Meta:
        model = Date
        fields = '__all__'

class MediaForm(EventForm):
    class Meta:
        model = Media
        fields = '__all__'

class PubForm(EventForm):
    class Meta:
        model = Publication
        fields = '__all__'