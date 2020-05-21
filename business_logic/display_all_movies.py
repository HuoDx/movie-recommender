from data import movies
from utils.ui import display_options

def display():
    print("All movies: %s"%", ".join(movies.get_all_movies()))
    c = input("Type enter to continue...")