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


# function which pulls Aucousticness from audio features
# using track ID.
def Acousticness(trackID) -> float:
    """
    Inputs:
        trackID = unique trackID of a track
    Returns:
        acousticness = float between 0.0 - 1.0 which
        represents the track's 'acousticness'
    """
    audioFeatures = sp.audio_features([trackID])
    if audioFeatures and audioFeatures[0] is not None:
        acousticness = audioFeatures[0]['acousticness']
        return acousticness
    else:
        return None
# ------------------------------------------------------------------


# function for pulling danceability
def Danceability(trackID) -> float:
    """
    Inputs:
        trackID = unique trackID of a track
    Returns:
        danceability = float between 0.0 - 1.0 which
        represents the track's 'danceability'
    """
    audioFeatures = sp.audio_features([trackID])
    if audioFeatures and audioFeatures[0] is not None:
        danceability = audioFeatures[0]['danceability']
        return danceability
    else:
        return None
# ------------------------------------------------------------------


# function for pulling duration of song
def Duration(trackID) -> float:
    """
    Inputs:
        trackID = unique trackID of a track
    Returns:
        duration = duration of song in ms
    """
    audioFeatures = sp.audio_features([trackID])
    if audioFeatures and audioFeatures[0] is not None:
        duration = audioFeatures[0]['duration_ms']
        return duration
    else:
        return None
# ------------------------------------------------------------------


# function for pulling energy of track
def Energy(trackID) -> float:
    """
    Inputs:
        trackID = unique trackID of a track
    Returns:
        energy = 'energy' song, float in range 0 - 1
    """
    audioFeatures = sp.audio_features([trackID])
    if audioFeatures and audioFeatures[0] is not None:
        energy = audioFeatures[0]['energy']
        return energy
    else:
        return None
# ------------------------------------------------------------------


# function for pulling instrumentallness
def Instrumentalness(trackID) -> float:
    """
    Inputs:
        trackID = unique trackID of a track
    Returns:
        instrumentallness = track's 'instrumentalness', float in range 0 - 1
    """
    audioFeatures = sp.audio_features([trackID])
    if audioFeatures and audioFeatures[0] is not None:
        instrumentalness = audioFeatures[0]['instrumentalness']
        return instrumentalness
    else:
        return None
# ------------------------------------------------------------------


# function for pulling liveness of track
def Liveness(trackID) -> float:
    """
    Inputs:
        trackID = unique trackID of a track
    Returns:
        liveness = liveness of 'track', float between 0-1
    """
    audioFeatures = sp.audio_features([trackID])
    if audioFeatures and audioFeatures[0] is not None:
        liveness = audioFeatures[0]['liveness']
        return liveness
    else:
        return None
# ------------------------------------------------------------------


# function for pulling loudness of track
def Loudness(trackID) -> float:
    """
    Inputs:
        trackID = unique trackID of a track
    Returns:
        loudness = loudness of 'track', float between 0-1
    """
    audioFeatures = sp.audio_features([trackID])
    if audioFeatures and audioFeatures[0] is not None:
        loudness = audioFeatures[0]['loudness']
        return loudness
    else:
        return None
# ------------------------------------------------------------------


# function for pulling speechiness of track
def Speechiness(trackID) -> float:
    """
    Inputs:
        trackID = unique trackID of a track
    Returns:
        speechiness = speechiness of 'track', float between 0-1
    """
    audioFeatures = sp.audio_features([trackID])
    if audioFeatures and audioFeatures[0] is not None:
        speechiness = audioFeatures[0]['speechiness']
        return speechiness
    else:
        return None
# ------------------------------------------------------------------


# function for pulling Valence of track
def Valence(trackID) -> float:
    """
    Inputs:
        trackID = unique trackID of a track
    Returns:
        valence = valence of 'track', float between 0-1
    """
    audioFeatures = sp.audio_features([trackID])
    if audioFeatures and audioFeatures[0] is not None:
        valence = audioFeatures[0]['valence']
        return valence
    else:
        return None
# ------------------------------------------------------------------


# function GetAll() returns all audio features of given track
def GetAllFeaturesAsDic(trackID) -> dict:
    TrackFeatures = {
            'Acousticness': Acousticness(trackID),
            'Danceability': Danceability(trackID),
            'Duration': Duration(trackID),
            'Energy': Energy(trackID),
            'Instrumentalness': Instrumentalness(trackID),
            'Livenss': Liveness(trackID),
            'Loudness': Loudness(trackID),
            'Speechiness': Speechiness(trackID),
            'Valence': Valence(trackID),
            }

    return TrackFeatures
# ------------------------------------------------------------------


# function GetAll() returns all audio features of given track
def GetAllFeaturesAsList(trackID) -> list:
    TrackFeatures = [
            Acousticness(trackID),
            Danceability(trackID),
            Duration(trackID),
            Energy(trackID),
            Instrumentalness(trackID),
            Liveness(trackID),
            Loudness(trackID),
            Speechiness(trackID),
            Valence(trackID),
            ]

    return TrackFeatures


tracks = GetTrackIDs()
print(tracks[0])
