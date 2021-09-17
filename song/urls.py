from django.urls import path
from .views import AddArtistAlbumsScraping, AddAlbumsSongsScraping

app_name = 'song'

urlpatterns = [
    path('add_artist_albums/', AddArtistAlbumsScraping.as_view(), name='add_artist_albums'),
    path('add_albums_songs/', AddAlbumsSongsScraping.as_view(), name='add_albums_songs'),
]
