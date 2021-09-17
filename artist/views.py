from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist
from scraping import Scraping
from darkflow.helper import create_file_by_url


class AddScrapingArtistToDB(APIView):

    def post(self, request):
        scp = Scraping()
        artists = scp.get_radiojavan_artists()
        for artist in artists:
            artist_obj = Artist()
            artist_obj.name = artist['name']
            create_file_by_url(artist['image'], artist_obj.image)
            artist_obj.save()
        return Response({})
