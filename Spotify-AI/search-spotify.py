"""
Using the search api call (spotipy.search()):
"""
from dotenv import load_dotenv
import json
from collect_filters import write_file, get_client


load_dotenv()
FILES_PREFIX = './Spotify-AI/files'


def open_file(filename: str):

    # doing as you do.
    try:
        with open(f"{FILES_PREFIX}/{filename}") as f:
            genres = json.load(f)

    # just copying you
    except Exception as e:
        print(e)
        raise e

    return genres


# using the search api call to hopefully get track id's with their features
def get_tracks(sp, query: str, batch_size: int):
    return sp.search(q=query, type='track', limit=batch_size)


def main() -> None:
    sp = get_client()
    data = open_file(filename='genres.json')
    genres = data['genres']
    # the query. Really weird sytnax tbh
    query = f'genres:{genres[0]}'

    # api call
    tracks = get_tracks(sp, query=query, batch_size=1)
    trackID = tracks['tracks']['items'][0]['id']

    write_file(data=trackID, filename='tracks.json', mode='w')

    return None


main()
