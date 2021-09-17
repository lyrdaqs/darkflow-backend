import requests
from bs4 import BeautifulSoup
from radiojavanapi import Client


class Scraping:
    def __init__(self):
        self.URL = "https://www.radiojavan.com/playlists/browse/Artists"
        self.artists = []

    def get_radiojavan_artists(self):
        page = requests.get(self.URL)
        soup = BeautifulSoup(page.content, "html.parser")
        artists_items = soup.find("div", class_="playlist_container").find_all("a", class_="play_all")
        for artist in artists_items:
            image = artist.find("img")['data-src']
            name = artist.find("span").text.split('of ')[1]
            artist_item = {
                'image': image,
                'name': name
            }
            self.artists.append(artist_item)
        return self.artists 


    def get_album_by_id(self, id):
        client = Client()
        album = client.get_album_by_id(id)
        return album

    
    def get_artist_by_name(self, name):
        client = Client()
        artist = client.get_artist_by_name(name)
        return artist
    



