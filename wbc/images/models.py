from django.db import models
from wbc.core.models import Model

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Album(Model):
    name        = models.CharField(blank=False, null=True, max_length=64, verbose_name="Name")
    cover_photo = models.ForeignKey('Photo', related_name='cover', blank=True, null=True)

    def __unicode__(self):
        if self.name:
            return self.name
        else:
            return 'Album Obj'
    
    def get_cover_photo(self):
        if self.cover_photo:
            return self.cover_photo
        else:
            return Photo.objects.filter(album=self).first()


class Photo(Model):
    album         = models.ForeignKey(Album)
    file          = models.ImageField(upload_to='project_images')
    thumbnail     = ImageSpecField(source="file", processors=[ResizeToFill(100,100)], format='JPEG', options={'quality':60})
    thumbnail_lg  = ImageSpecField(source="file", processors=[ResizeToFill(400,300)], format='JPEG', options={'quality':60})
    thumbnail_map = ImageSpecField(source="file", processors=[ResizeToFill(320,180)], format='JPEG', options={'quality':60})
    image_sidebar = ImageSpecField(source="file", processors=[ResizeToFill(1280,720)], format='JPEG', options={'quality':60})