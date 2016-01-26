try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from registration.backends.default.views import RegistrationView, ActivationView

from .forms import ProfileForm, UserForm
from wbc.stakeholder.forms import StakeholderProfileForm

from .models import *

def profile(request, pk):
    p = get_object_or_404(Profile, pk= int(pk))
    return render(request, 'accounts/user_profile.html', {
        'profile': p    
    })


@login_required
def profile_update(request):
    # next = request.META.get('HTTP_REFERER', '')
    #always redirect to user profile after save
    next = reverse('stakeholder', kwargs={'slug':request.user.profile.stakeholder.slug})

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        stakeholder_form = StakeholderProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid() and stakeholder_form.is_valid():
            request.user.first_name = user_form.cleaned_data['first_name']
            request.user.last_name = user_form.cleaned_data['last_name']
            request.user.email = user_form.cleaned_data['email']
            request.user.save()

            for field in request.user.profile.get_fields():
                setattr(request.user.profile, field, profile_form.cleaned_data[field])
            request.user.profile.save()

            for field in request.user.profile.stakeholder.get_fields():
                setattr(request.user.profile.stakeholder, field, stakeholder_form.cleaned_data[field])
            request.user.profile.stakeholder.save()

            next = request.POST.get('next', '')
            path = urlparse(next).path
            if path in ['', reverse('login'), reverse('profile_update')]:
                return HttpResponseRedirect(reverse('start'))
            else:
                return HttpResponseRedirect(next)
    else:
        user_initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email
        }

        profile_initial = request.user.profile.as_dict()
        stakeholder_initial = request.user.profile.stakeholder.as_dict()

        user_form = UserForm(initial=user_initial)
        profile_form = ProfileForm(initial=profile_initial)
        stakeholder_form = StakeholderProfileForm(initial=stakeholder_initial)


    return render(request, 'accounts/profile_form.html', {'user_form': user_form, 'profile_form': profile_form, 'stakeholder_form': stakeholder_form, 'next': next})


class WbcRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return reverse('profile', user.pk)