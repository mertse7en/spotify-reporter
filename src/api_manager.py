import json
import logging
import os, sys
import pandas as pd
import spotipy

from spotipy.oauth2 import SpotifyOAuth
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(funcName)s - %(message)s")


class APIManager:
    def __init__(self):
        # Logger
        self.logger = logging.getLogger(self.__class__.__name__)

        # API creds
        self.client_id = os.environ["CLIENT_ID"]
        self.client_secret = os.environ["CLIENT_SECRET"]
        self.redirect_uri = os.environ["REDIRECT_URI"]
        self.scope = "user-library-read"

        # SP Instance
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.client_id,
                                                            client_secret=self.client_secret,
                                                            redirect_uri=self.redirect_uri,
                                                            scope="user-read-recently-played"))


    def get_recently_played_df(self):
        # Get the latest after time stamp
        after = "1637360567294"
        played_songs = self.sp.current_user_recently_played(limit=50, after="1637360567294")
        
        # Write json to check json element on "https://jsonformatter.curiousconcept.com/"
        # with open('example.json', 'w') as f:
        #     json.dump(played_songs, f)

        items = played_songs["items"] # List
        after_cursor = played_songs["cursors"] # Push after_cursor timestamp to db in order to find correct time interval in next commit 
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
        print("-"*100)

        song_name = list() 
        song_id = list() 
        song_popularity = list() 
        song_preview_url = list() 
        song_spotify_url = list() 
        
        album_name = list() # id 
        album_id = list() # name
        album_spotify_url = list()

        artist_name = list()
        artist_id = list()
        artist_spotify_url = list()

        for song_metadata in items:

            album_name.append(song_metadata["track"]["album"]["id"])
            album_id.append(song_metadata["track"]["album"]["id"])
            album_spotify_url.append(song_metadata["track"]["album"]["id"])
            
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

            song_name.append(song_metadata["track"]["name"])
            song_id.append(song_metadata["track"]["id"])
            song_popularity.append(song_metadata["track"]["popularity"])
            song_preview_url.append(song_metadata["track"]["preview_url"])
            song_spotify_url.append(song_metadata["track"]["external_urls"]["spotify"])

            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

            artists = song_metadata["track"]["artists"]
            if(len(artists) != 1):
                artist_name.append(artists[0]["name"])
                artist_id.append(artists[0]["id"])
                artist_spotify_url.append(artists[0]["external_urls"]["spotify"])
            else:
                for artist_metadata in artists:
                    artist_name.append(artist_metadata["name"])
                    artist_id.append(artist_metadata["id"])
                    artist_spotify_url.append(artist_metadata["external_urls"]["spotify"])

        # Last cursor
        cursors = played_songs["cursors"]

        df = pd.DataFrame({
            "song_name": song_name,
            "artist_name": artist_name,
            "song_id": song_id,
            "song_popularity": song_popularity,
            "song_preview_url": song_preview_url,
            "song_spotify_url": song_spotify_url,
            "album_name": album_name,
            "album_id": album_id,
            "album_spotify_url": album_spotify_url,
            
            "artist_id": artist_id,
            "artist_spotify_url": artist_spotify_url
        })

        return df



