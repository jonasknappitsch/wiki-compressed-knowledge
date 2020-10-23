import wikipedia
import random

def get_most_popular_by_topic(SEARCH,suggest):
    return wikipedia.search(SEARCH,results=RESULTS,suggestion=suggest)

def get_summary(SEARCH):
    try:
        print(wikipedia.summary(SEARCH))
    except wikipedia.exceptions.DisambiguationError as e:
        # TODO
        #print('Random choice: ', random.choice(e.options))
        #print('Wikipedia.page: ', wikipedia.page(random.choice(e.options)))
        print('Did you mean',e.options,'?')

# final values
SEARCH = '1sb1951ndxks'
RESULTS = 5

most_popular = get_most_popular_by_topic(SEARCH,True)

if(most_popular[0]):
    print('Most popular results: ',most_popular[0])

if(most_popular[1]):
    print('Did you mean',most_popular[1],'? Answer with 0 or 1')
    if(int(input())):
        SEARCH = most_popular[1]
        print(get_most_popular_by_topic(SEARCH,False))
else:
    if not(most_popular[0]):
        print('Sorry, we could not find any articles.')
    
#print(get_summary(SEARCH))