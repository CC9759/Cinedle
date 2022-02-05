"""
Functions for acquiring imdb information
"""
import imdb
import random

imdb_data = imdb.IMDb()

def  get_top250():
    return imdb_data.get_top250_movies()

def get_rand_movie():
    return get_top250()[random.randrange(250)]

def check_movie(user_input, answer):
    print(answer)
    movies = imdb_data.search_movie(user_input)

    return movies != None and movies[0]['title'] == answer['title']

