from django.db import models
from account.models import CustomUser
from song.models import Song
from darkflow.helper import music_style



class Artist(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    style = models.CharField(max_length=2, 
                    choices=music_style.STYLES, default='OT')

    def __str__(self):
        return self.name

