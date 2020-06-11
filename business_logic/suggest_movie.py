from data import movies
from utils.ui import display_options
from requests_html import HTMLSession
import random

def suggest():
    # print("what's up")
	# Start coding here
    print('Searching for Movies......')
    session = HTMLSession()
    url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
    # print("here")
    r = session.get(url)
    names = []
    n=0
    try:
        while True:
            n+=1
            thing = '#main > div > span > div > div > div.lister > table > tbody > tr:nth-child('+str(n)+') > td.titleColumn'
            position=r.html.find(thing)
            name = position[0].text
            name = name.split()
            new_name = ''
            for i in range(len(name)):
                if i != 0:
                    new_name += name[i]+' '
            new_name = new_name.strip()
            names.append(new_name)
            #print(position)
            #print(new_name)
    except TypeError as te:
	    pass
        #This is normal, according to Eric C
    except IndexError as ie:
        pass
        #This seems also normal according to Eric C

    length = len(names)
    random_number = random.randint(0,length+1)



    # print(length)
    # print(names)
    print(names[random_number])
    
    pass