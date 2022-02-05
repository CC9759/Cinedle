import imdb
import random

def get_rand_movie():
    imdb_data = imdb.IMDb()

    top250 = imdb_data.get_top250_movies()
    return top250[random.randrange(250)]

def test():
    print(get_rand_movie())

test()