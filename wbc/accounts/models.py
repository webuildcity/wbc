from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return str(self.user.username)

    def __unicode__(self):
        return unicode(self.__str__())

    class Meta:
        ordering = ("user",)
        verbose_name = "Benutzerkonto"
        verbose_name_plural = "Benutzerkonten"