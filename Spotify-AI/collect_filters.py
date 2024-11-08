import json

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

# The folder where I'm going to store the jsons
# If you run the program from inside the Spotify-AI folder, you'll have to remove the Spotify-AI part
FILES_PREFIX = "./Spotify-AI/files"


# Get the spotipy client
def get_client():
    auth_manager = SpotifyClientCredentials()
    return spotipy.Spotify(auth_manager=auth_manager)


# Get the genres - ??
# Not really sure how this works, might be specific to my account
# Not sure if this is a complete list of Spotify genres
def get_genre_seeds(sp):
    return sp.recommendation_genre_seeds()


# param: type are type hints in python. Won't cause errors if the params end up being the wrong type but can help readability
def write_file(data: json, filename: str, mode: str):
    # File stuff can be prone to failure, so wrapping in try - except block to catch any errors
    try:
        # Open the file and dump the data to it as a json
        with open(f"{FILES_PREFIX}/{filename}", mode) as f:
            json.dump(data, f)

    # Exception will catch any type of exception. You can use other types for more specific use cases
    except Exception as e:
        # Print the error for debugging
        print(e)
        # propagate the error to let the program fail
        raise e


# TODO not 100% sure I'm getting all the categories avaliable. And at least 1 category name might have an encoding problem
def get_categories(sp):
    # Single line function to get the names from the dictionary response
    extract_category_names = lambda x: [x["name"] for x in x["categories"]["items"]]

    # This call uses pagination - will track with this variable
    index = 0

    all_names = []

    while True:
        # Get the first page of categories - max results = 50, offset = pagination
        res = sp.categories(limit=50, offset=index)

        # print(res)

        names = extract_category_names(res)

        all_names += names

        # When there are no more categories the response will return an empty list for items
        # and names will become empty as a result. Empty lists evaluate as false.
        if not names:
            break

        # Increment the pagination
        index += 1

    # Noticed duplicate names at first. Casting to set will remove them.
    # but set can't be converted to JSON to back to list we go
    # sorted for alphabetical order
    return sorted(list(set(all_names)))


def main():
    # Get the spotipy client
    sp = get_client()
    # Get a list of genres
    genres = get_genre_seeds(sp)
    # Save the genres to the file folder - I think this list will be the same everytime
    # so the file open mode should be in overwrite so I don't get duplicates
    write_file(data=genres, filename="genres.json", mode="w")

    # Not really sure what categories are
    categories = get_categories(sp)

    # Write categories to a file
    write_file({"categories": categories}, "category_names.json", "w+")


main()
