import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import dotenv_values


creds = dotenv_values('.env')
scope = 'user-library-read'
sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=creds['SPOTIPY_CLIENT_ID'],
            client_secret=creds['SPOTIPY_CLIENT_SECRET'],
            redirect_uri=creds['SPOTIPY_REDIRECT_URI'],
            scope=scope,
            )
        )


def get_saved_track_ids():
    track_ids = []
    offset = 0
    limit = 50  # max limit per request

    while True:
        # Fetch saved tracks with offset and limit
        results = sp.current_user_saved_tracks(limit=limit, offset=offset)

        # Extract track IDs from the results
        for item in results['items']:
            track_id = item['track']['id']
            track_ids.append(track_id)

        # Check if there are more tracks to fetch
        if results['next'] is None:
            break

        # Update offset to get the next batch of tracks
        offset += limit

    return track_ids


# Get saved track IDs
track_ids = get_saved_track_ids()
print("Saved Track IDs:", track_ids)
