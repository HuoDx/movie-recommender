from data import movies
from utils.ui import display_options
#haha! michael j was here
def  adjust_sorting():
    # Start coding here
    stored_movies=movies.get_all_movies()
    print("Your current list is")
    for term in range(len(stored_movies)):
        print(str((term+1))+', '+stored_movies[term])
    firstindex=eval(input('''What's the number of the first movie you want to switch: '''))-1
    secondindex=eval(input('''What's the number of the first movie you want to switch: '''))-1
    stored_movies[firstindex],stored_movies[secondindex]=stored_movies[secondindex],stored_movies[firstindex]
    print(stored_movies)




    
    pass
