# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from wbc.core.views import ProtectedCreateView, ProtectedUpdateView, ProtectedDeleteView
from wbc.blog.models import BlogEntry
from models import *
from forms import *


def blogentry(request, slug):
    b = BlogEntry.objects.get(slug__iexact=slug)
    return render(request, 'blog/blogentry.html', {'b' : b})

class BlogView(TemplateView):

    template_name="blog/blog.html"

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        blogEntries = BlogEntry.objects.all().order_by('-created')
        context['blogentries'] = blogEntries
        return context

class BlogEntryCreate(ProtectedCreateView):
    model = BlogEntry
    form_class = BlogEntryForm

    def form_valid(self, form):
        self.object = form.save()
        url = self.object.get_absolute_url()
        return JsonResponse({'redirect':  url})

    def form_invalid(self, form):
        response = super(BlogEntryCreate, self).form_invalid(form)
        return response

class BlogEntryUpdate(ProtectedUpdateView):
    model = BlogEntry
    form_class = BlogEntryForm

    def form_valid(self, form):
        self.object = form.save()
        url = self.object.get_absolute_url()
        return JsonResponse({'redirect':  url})

    def form_invalid(self, form):
        response = super(BlogEntryUpdate, self).form_invalid(form)
        return response

class BlogEntryDelete(ProtectedDeleteView):
    model = BlogEntry
    success_url = reverse_lazy('blog')
