import imdb
import random

imdb_data = imdb.IMDb()

def  get_top250():
    return imdb_data.get_top250_movies()

def get_rand_movie():
    return get_top250[random.randrange(250)]

print(get_rand_movie())