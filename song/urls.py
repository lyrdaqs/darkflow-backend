from django.urls import path
from .views import AddArtistAlbumsScraping, AddAlbumsSongsScraping, SongDetail

app_name = 'song'

urlpatterns = [
    path('add_artist_albums/', AddArtistAlbumsScraping.as_view(), name='add_artist_albums'),
    path('add_albums_songs/', AddAlbumsSongsScraping.as_view(), name='add_albums_songs'),
    path('<int:pk>/', SongDetail.as_view(), name='song_detail'),
]
