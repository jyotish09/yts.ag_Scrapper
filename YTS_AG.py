import requests
from bs4 import BeautifulSoup as BS
import re

session = requests.session()
page = session.post('https://yts.ag/')

#Home Page details

#Popular Movies

popular_movies = BS(page.text,"html.parser").find('div',{'id':'popular-downloads'})
##print(popular_movies)
popular_movies_rating = popular_movies.find_all('h4',{'class':'rating'})
popular_movies = popular_movies.find_all('a',{'class':'browse-movie-title'})

##print(popular_movies)
##print('\n')

pMR=[]

for i in popular_movies_rating:
    pMR.append(re.search('(\d+\.\d+)',i.get_text()).group())

##print (pMR)
print('\n')


pM=[]

for i in popular_movies:
    pM.append(re.search('(.+)',i.get_text()).group())


print ('Trending Downloads in YTS: ' + '\n')

for i,j in zip(pM,pMR):
    print(i+" - (Rotten Tomatoes : "+j+")")

print('\n')


#Latest Movies

