from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

def validate_email_unique(value):
    exists = User.objects.filter(email=value)
    if exists:
        raise ValidationError("Email address %s already exists, must be unique" % value)

def validate_username_unique(value):
    exists = User.objects.filter(username=value)
    if "@" in value:
        raise ValidationError("@ not allowed in username")
    if exists:
        raise ValidationError("Username %s already exists, must be unique" % value)