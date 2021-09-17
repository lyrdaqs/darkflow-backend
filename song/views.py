from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Song, Album
from artist.models import Artist
from scraping import Scraping
from darkflow.helper import create_file_by_url


class AddArtistAlbumsScraping(APIView):

    def post(self, request):
        scp = Scraping()
        artists = Artist.objects.all()
        for artist in artists:
            print(artist.name)
            artist_scp = scp.get_artist_by_name(artist.name)
            for album in artist_scp.albums:
                Album.objects.create(uuid=album.id, artist=artist, name=album.name)
        
        return Response({})


class AddAlbumsSongsScraping(APIView):
    
    def post(self, request):
        scp = Scraping()
        albums = Album.objects.all()
        for album in albums:
            print(album.name)
            album_scp = scp.get_album_by_id(album.uuid)
            for track in album_scp.tracks:
               artist = Artist.objects.get(name=track.artist)
               song_obj = Song()
               song_obj.name = track.name
               song_obj.duration = str(track.duration)
               song_obj.lyrics = track.lyric
               song_obj.artist = artist
               song_obj.album = album
               create_file_by_url(track.hq_link, song_obj.play)
               create_file_by_url(track.photo, song_obj.cover)
               song_obj.save()
        
        return Response({})

