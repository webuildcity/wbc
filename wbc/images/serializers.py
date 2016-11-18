# -*- coding: utf-8 -*-
from rest_framework import serializers

from models import *

class AlbumSerializer(serializers.ModelSerializer):
    photos =  serializers.SerializerMethodField('photos_serializer')

    def photos_serializer(self, obj):
        photos_array = []
        for photo in obj.photo_set.all():
            photos_array.append({ 
                'url': photo.file.url,
                'h': photo.file.height,
                'w': photo.file.width
            })
        return photos_array
    

    class Meta:
        model = Album
        fields = ('name','photos')
