"""
Functions for acquiring imdb information
"""
import imdb
import random

imdb_data = imdb.IMDb()


def get_top250():
    return imdb_data.get_top250_movies()


def get_rand_movie():
    return get_top250()[random.randrange(250)]

def get_user_movie(user_input):
    return imdb_data.search_movie(user_input)[0]['title']


def check_movie(user_input, answer):
    movies = imdb_data.search_movie(user_input)
    return movies is not None and movies[0]['title'] == answer['title']
