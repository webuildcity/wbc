from django.db import models

class Project(models.Model): 
    titel       = models.CharField(max_length=256)
    traeger     = models.CharField(max_length=256)
    typ         = models.CharField(max_length=256)
    bezirke     = models.CharField(max_length=256)
    lon         = models.FloatField()
    lat         = models.FloatField()
    status      = models.CharField(max_length=256)
    publikation = models.CharField(max_length=256)
    datum       = models.DateTimeField()
    link        = models.URLField()

    def __unicode__(self):
        return '[' + unicode(self.id) + '] ' + self.titel
        
class BBP(models.Model): 
    vorhaben    = models.CharField(max_length=256)
    bplan       = models.CharField(max_length=256)
    typ         = models.CharField(max_length=256)
    bezirke     = models.CharField(max_length=256)
    lon         = models.FloatField()
    lat         = models.FloatField()
    begin       = models.DateTimeField()
    end         = models.DateTimeField()
    ort         = models.CharField(max_length=256)
    zeiten      = models.CharField(max_length=256)
    link        = models.URLField()    

    def __unicode__(self):
        return '[' + unicode(self.id) + '] ' + self.vorhaben
