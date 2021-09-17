from django.urls import path
from .views import AddScrapingArtistToDB

app_name = 'artist'

urlpatterns = [
    path('scraping/', AddScrapingArtistToDB.as_view(), name='scraping_artist'),
]
