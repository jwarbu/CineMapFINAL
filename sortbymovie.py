# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
from time import sleep
import json
import operator

# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
from time import sleep

enter_zipcode = input("Please enter your zipcode:")

url = "https://www.google.com/movies?near=" + enter_zipcode +"&sort=1"
#url = "https://www.google.com/movies?near=02446&sort=1"

print(url)

soup = BeautifulSoup(requests.get(url).text, "html5lib")

movie_results = soup.find_all('div', attrs={'class':'movie'})
#print (len(theater_results))
# 10 theaters
movie_name_all = []
movie_info_all = []
theater_combo_all = []


for div in movie_results:

    theater_name_all = []
    theater_info_all = []
    theater_showtime_all = []

    movie_name = div.find('h2', attrs={'itemprop':'name'}).text
    movie_name_all.append(movie_name)
    movie_info = div.find_all('div', attrs={'class': 'info'})[1].contents[0].strip()
    movie_info_all.append(movie_info)

    theater_name = div.find_all('div', attrs={'class':'name'})
    theater_info = div.find_all('div', attrs={'class':'address'})
    theater_showtime = div.find_all('div', attrs={'class':'times'})

    for item in theater_name:
        theater_name_indiv = item.text
        theater_name_all.append(theater_name_indiv)

    for item in theater_info:
        theater_info_indiv = item.text
        theater_info_all.append(theater_info_indiv)

    for item in theater_showtime:
        theater_showtime_indiv = item.text
        theater_showtime_all.append(theater_showtime_indiv)


    theater_zip = list(zip(theater_name_all, theater_info_all, theater_showtime_all))
    theater_combo = '\n'.join('\t{}\n\t{}\n\t{}\n'.format(*item) for item in theater_zip)
    theater_combo_all.append(theater_zip)

movie_combo = list(zip(movie_info_all, theater_combo_all))
#movie_combo_str = '\n'.join('{}\n{}\n'.format(*item) for item in movie_zip)

#print(movie_listing['Suicide Squad'])
omdb_title_all = []
metascore_all = []

for item in movie_name_all:
    googletitle = '+'.join(item.split()).strip('3D')
    omdburl = "http://www.omdbapi.com/?t=" + googletitle + "&plot=short&r=json&tomatoes=true"

    #omdburl = "http://www.omdbapi.com/?t=suicide+squad&plot=short&r=json&tomatoes=true"

    #print(omdburl)

    omdbsoup = BeautifulSoup(requests.get(omdburl).text, "html5lib")

    json_string = omdbsoup.text
    #print(json_string)

    parsed_json = json.loads(json_string)
    omdb_title = parsed_json["Title"]
    omdb_title_all.append(omdb_title)

    metascore = parsed_json["Metascore"]
    metascore_all.append(metascore)


omdb_dict = {}
omdb_dict = dict(zip(omdb_title_all, metascore_all))

#print(metascore_all)
final_combo = list(zip(metascore_all, movie_combo))
movie_listing = {}
movie_listing = dict(zip(movie_name_all, final_combo))

movie_listing_x = sorted(movie_listing.items(), key=operator.itemgetter(1), reverse=True)
print(movie_listing_x[0], '\n\n', movie_listing_x[1], '\n\n', movie_listing_x[2], '\n\n', movie_listing_x[3], '\n\n', movie_listing_x[4], '\n\n', movie_listing_x[5], '\n\n', movie_listing_x[6],'\n\n', movie_listing_x[7], '\n\n', movie_listing_x[8], '\n\n', movie_listing_x[9])