from django.db import models
from song.models import Song, Album
from artist.models import Artist


class Search:
    def __init__(self, keyword):
        self.keyword = keyword
        self.artists_search = None
        self.albums_search = None
        self.songs_search = None
    
    def search_engine(self):
        if self.keyword == None:
            self.keyword = ''
        songs = Song.objects.filter(name__icontains=self.keyword)
        albums = Album.objects.filter(name__icontains=self.keyword)
        artists = Artist.objects.filter(name__icontains=self.keyword)
        self.albums_search = albums
        self.artists_search = artists
        self.songs_search = songs
        return self
