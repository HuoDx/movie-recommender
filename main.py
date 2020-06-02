from business_logic.add_movie import add
from business_logic.display_all_movies import display
from business_logic.adjust_sort import adjust_sorting
from business_logic.sort_movies import sort_movies
from business_logic.suggest_movie import suggest
from utils.ui import display_options

# Mary

while True:
    display_options({
        "Add Movies": add,
        "Show Movies": display,
        'Sort Movies': sort_movies,
        'Adjust Sorting': adjust_sorting,
        'Recommend a Movie': suggest
    })
