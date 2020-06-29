
stored_movies = []

# Load data from file
# Start coding here


def save_to_file():
    global stored_movies
    # Save data to file
    # Start coding here
    f = open('stored_movies.txt', 'w', encoding=‘utf-8’)
    for movie in stored_movie:
        f.write(movie)
        f.write("\n")



def add_movie(movie):
    global stored_movies
    stored_movies.append(movie)
    save_to_file()

def get_all_movies():
    global stored_movies
    return stored_movies