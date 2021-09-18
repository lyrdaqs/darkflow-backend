from rest_framework import serializers
from artist.serializers import ArtistSerializer
from song.serializers import SongSerializer, AlbumSerializer


class SearchSerializer(serializers.Serializer):
    artists = serializers.SerializerMethodField(read_only=True)
    songs = serializers.SerializerMethodField(read_only=True)
    albums = serializers.SerializerMethodField(read_only=True)

    def get_artists(self, obj):
        serializer = ArtistSerializer(obj.artists_search,many=True)
        return serializer.data 

    def get_albums(self, obj):
        serializer = AlbumSerializer(obj.albums_search,many=True)
        return serializer.data 

    def get_songs(self, obj):
        serializer = SongSerializer(obj.songs_search,many=True)
        return serializer.data 