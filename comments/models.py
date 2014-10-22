import urllib
import hashlib

from django.db import models
from lib.models import Model

from projects.models import Ort

class Kommentar(models.Model):
    ort = models.ForeignKey(Ort)
    
    author_name  = models.CharField(max_length=100)
    author_email = models.CharField(max_length=256)
    author_url   = models.CharField(max_length=256)

    enabled = models.BooleanField()
    content = models.TextField()

    @property
    def gravatar(self):
        gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(self.author_email.lower()).hexdigest() + "?"
        gravatar_url += urllib.urlencode({'s':str(32)})

        return gravatar_url
