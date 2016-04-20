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
popular_movies_torrents = popular_movies.find_all('a',{'rel':'nofollow'})

tempList = popular_movies.find_all('div',{'class':'browse-movie-tags'})
tempList_torrents =[]

for i in tempList:
    torrents = i.find_all('a',{'rel':'nofollow'})
    if (len(torrents) == 2):
        tempList_torrents.append({'720p':(re.search('(.+)',torrents[0]['href']).group()),'1080p':(re.search('(.+)',torrents[1]['href']).group())})
    else :
        tempList_torrents.append({'720p':(re.search('(.+)',torrents[0]['href']).group()),'1080p':''})

popular_movies = popular_movies.find_all('a',{'class':'browse-movie-title'})

##print(popular_movies)
##print('\n')

##print(popular_movies_torrents)

print(tempList_torrents)
print('\n')

pMT1080p=[]
pMT720p=[]


for i in popular_movies_torrents:
    if(i.get_text()=='1080p'):
        pMT1080p.append(re.search('(.+)',i['href']).group())
    if (i.get_text()=='720p'):
        pMT720p.append(re.search('(.+)',i['href']).group())
        
##print(pMT1080p)
##print(pMT720p)


pMR=[] ##popular_movies_rating

for i in popular_movies_rating:
    pMR.append(re.search('(\d+\.\d+)',i.get_text()).group())

##print (pMR)
print('\n')


pM=[]  ##popular_movies

for i in popular_movies:
    pM.append(re.search('(.+)',i.get_text()).group())


print ('Trending Downloads in YTS: ' + '\n')

for i,j,k,l in zip(pM,pMR,pMT1080p,pMT720p):
    print(i+" - (Rotten Tomatoes : "+j+")")
    print('1080p Link : '+k)
    print('720p Link : '+l+ '\n')

print('\n')


#Latest Movies

latest_movies = BS(page.text,"html.parser").find('div',{'class':'home-movies'})
##print(latest_movies)
