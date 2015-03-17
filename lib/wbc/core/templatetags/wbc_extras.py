# -*- coding: utf-8 -*-
from markdown import markdown as mdn

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def markdown(value):
    value = force_unicode(value)
    return mdn(value)
