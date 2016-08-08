import requests
from bs4 import BeautifulSoup
import urllib


r= requests.get('https://www.google.com/movies?near=02446')
# resp = requests.post('https://www.google.com/movies?near=02446')

#print (r.text)
soup = BeautifulSoup(r.text, "lxml")

print (soup.prettify()) # [0:1000]



