"""

==================
=== API test 1 ===
==================
fetch metadata from web api

"""
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import dotenv_values


credentials = dotenv_values(".env")
# scope defines what data the api reads from
scope = 'user-library-read'
# I guess this next part tells the API where to fetch info from
sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=credentials['SPOTIPY_CLIENT_ID'],
            client_secret=credentials['SPOTIPY_CLIENT_SECRET'],
            redirect_uri=credentials['SPOTIPY_REDIRECT_URI'],
            scope=scope,
            )
        )


# word on the street is that pagination is
# important (i.e. chat gpt says to do it)

# getting total number of tracks
results = sp.current_user_saved_tracks()
totalTracks = results['total']
offset = 0  # one of the parameters in current_user_saved_tracks functions
batchSize = 20
batchNumber = 0


# Defining the number of API calls needed to get entire playlist
if totalTracks % batchSize != 0:
    numberOfBatches = (totalTracks // batchSize) + 1
else:
    numberOfBatches = (totalTracks // batchSize)


# getting the metadata
while batchNumber <= numberOfBatches and offset <= totalTracks:

    savedSongs = sp.current_user_saved_tracks(limit=batchSize, offset=offset)
    print(f"\nBatch: {batchNumber}")

    for i in savedSongs['items']:
        track = i['track']
        artist_id = track['artists'][0]['id']
        artist = sp.artist(artist_id)
        genres = artist.get('genres', [])

        print(f"Name: {track['name']}")
        print(f"Artist: {track['artists'][0]['name']}")
        print(f"Album: {track['album']['name']}")
        print(f"Release Date: {track['album']['release_date']}")
        print(f"Genres: {genres}")
        print('\n')

    batchNumber += 1
    offset += 20
