#!/usr/bin/env python3
import re
from similarity.damerau import Damerau


def find_url_in_filename(filename: str) -> str:
    """ Find any URLs present in file name
    Args:
        filename (str): Filename
    Returns:
        str: URL 
    """
    url = re.findall(
        'www.(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\)]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
        filename
    )
    return url[0]


def remove_all_illegal_characters(filename: str) -> str:
    """ Remove illegal characters for a filename

    Args:
        filename (str): Filename

    Returns:
        str: Filename without illegl characters
    """
    illegal_characters = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for character in illegal_characters:
        filename = filename.replace(character, "")
    return filename


def find_most_apt(name: str, movies: list) -> str:
    damerau = Damerau()
    distances = []
    for movie in movies:
        # If the movie is an exact match
        if name.upper() == movie.upper():
            return movie
        # Else append similarity distance
        distances.append(damerau.distance(name.upper(), movie.upper()))
    idx = int(distances.index(min(distances)))
    most_closest_name = movies[idx]
    # If no match
    if most_closest_name == "":
        most_closest_name = name
    return most_closest_name
