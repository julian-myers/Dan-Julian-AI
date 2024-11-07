"""
Hopefully a list of useful functions
for interacting with the spotify web API.
"""
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import dotenv_values


credentials = dotenv_values(".env")
scope = 'user-library-read'
sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=credentials['SPOTIPY_CLIENT_ID'],
            client_secret=credentials['SPOTIPY_CLIENT_SECRET'],
            redirect_uri=['SPOTIPY_REDIRECT_URI'],
            scope=scope,
            )
        )


# ------------------------------------------------------------------
# function for getting the unique track id's
# from a user's saved tracks (liked songs)
def GetTrackIDs():
    """
    Inputs:
        None
    Returns:
        trackIDs = A full list of track ID's from
                   a user's saved tracks library
    """

    # getting total number of tracks for the sake of iteration
    results = sp.current_user_saved_tracks()
    totalTracks = results['total']
    offset, batchNumber, BatchSize = 0, 0, 20  # parameters for spotipy
    trackIDs = []

    # this determines the number of API calls needed
    if totalTracks % BatchSize != 0:
        numberOfBatches = (totalTracks // BatchSize) + 1
    else:
        numberOfBatches = (totalTracks // BatchSize)

    # API calls using pagination
    while batchNumber <= numberOfBatches or offset < totalTracks:

        savedTracks = sp.current_user_saved_tracks(
                limit=BatchSize,
                offset=offset
                )
        for track in savedTracks['items']:
            trackID = track['track']['id']
            trackIDs.append(trackID)

        offset += BatchSize
        batchNumber += 1

    return trackIDs
# ------------------------------------------------------------------
