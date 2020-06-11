from data import movies
from utils.ui import display_options

# Miranda.
def  sort_movies():
    # Start coding here
    unsorted = movies.get_all_movies()
    switched = True
    while switched:
        switched = False
        for i in range(len(unsorted)-1):
            user = input('Which one do you enjoy more? Enter 1 for '+str(unsorted[i])+' Enter 2 for '+str(unsorted[i+1]))
            if user == '2':
                switched = True
                unsorted[i],unsorted[i+1]=unsorted[i+1],unsorted[i]
    print(unsorted)

sort_movies()
#sara trying