from django.db import models
from account.models import CustomUser
from darkflow.helper import music_style


class Album(models.Model):
    name = models.CharField(max_length=200)
    artist = models.ForeignKey("artist.Artist", on_delete=models.PROTECT)
    uuid= models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Song(models.Model):
    cover = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=200)
    play = models.FileField()
    stream = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    duration = models.CharField(max_length=20)
    lyrics = models.TextField(null=True, blank=True)
    style = models.CharField(max_length=2, 
                    choices=music_style.STYLES, default='OT')
    artist = models.ForeignKey("artist.Artist", on_delete=models.PROTECT)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class History(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} played {self.song.name}'
