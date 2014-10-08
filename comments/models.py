from django.db import models

from projects.models import Verfahren
# Create your models here.

class Kommentar(models.Model):
    verfahren_id = models.ForeignKey(Verfahren)
    
    author_name  = models.CharField(max_length=100)
    author_email = models.CharField(max_length=256)
    author_url   = models.CharField(max_length=256)

    created_at = models.DateTimeField()

    enabled = models.BooleanField()
    content = models.TextField()
