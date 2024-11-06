"""

==================
=== API test 1 ===
==================
fetch metadata from web api

"""
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# credentials
clientID = 'b788aaad11de481dba3ce11bbb447a56'
clientSecret = '380d1cb0075644a38460e97ddba8efb3'
redirectURI = 'http://127.0.0.1:5000'


# scope defines what data the api reads from
scope = 'user-library-read'
# I guess this next part tells the API where to fetch info from
sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope=scope,
            client_id=clientID,
            client_secret=clientSecret,
            redirect_uri=redirectURI
            )
        )


# word on the street is that pagination is
# important (i.e. chat gpt says to do it)

# getting total number of tracks
results = sp.current_user_saved_tracks()
totalTracks = results['total']
offset = 0  # one of the parameters in current_user_saved_tracks functions
batchSize = 20
print('Number of Tracks: {totalTracks}')


# Defining the number of API calls needed to get entire playlist
if totalTracks % batchSize != 0:
    numberOfBatches = (totalTracks // batchSize) + 1
else:
    numberOfBatches = (totalTracks // batchSize)


# getting the metadata
while offset < totalTracks:
    sp.current_user_saved_tracks(limit=batchSize, offset=offset)

    for i in results['items']:
        track = i['track']
        artist_id = track['artists'][0]['id']
        artist = sp.artist(artist_id)
        genres = artist.get('genres', [])

        print(f"Name: {track['name']}")
        print(f"Artist: {track['artists'][0]['name']}")
        print(f"Album: {track['album']['name']}")
        print(f"Release Date: {track['album']['release_date']}")
        print(f"Genres: {genres}")
        print('楩楩楩楩楩楩楩楩楩楩楩楩楩楩楩楩楩楩楩楩楩楩楩楩楩')

    offset += batchSize
