import bs4
import requests
from bs4 import BeautifulSoup
import pickle
import regex as re 

'''
The Monticello website sells seeds and live plants (depending on season), and allows one to filter
by amount of sunlight required, annual vs. perennial, etc., but not by origin! In order to find
only plants from North America, the website is crawled upon and the descriptions of each plant scraped.
The resulting dictionary of tuples ("Plant name", "URL path") is pickled for quick access.

Further projects:
1) Automatically populate a database with all of every plants' information.
2) Set up automatic notifications when it's time to order seeds/plants for their respective planting seasons. 
'''

# UNCOMMENT BELOW to do a fresh scrape of the live site and pickle a new dictionary

'''
tj_site = 'https://www.monticelloshop.org/farm-garden-plants-all.html'

r = requests.get(tj_site)
soup = BeautifulSoup(r.content, 'html.parser')

regx = re.compile('[0-9]{6}\.html')
html_tags = soup.findAll('a', href=True)
plant_dict = {}
for tag in html_tags:
    if regx.match(tag['href']):
        plant_dict[tag['href']] = plant_dict.get(tag, 1)

plant_names = []

for key in plant_dict.keys():
    url = 'https://www.monticelloshop.org/' + key
    u = requests.get(url)
    soupy = BeautifulSoup(u.content, 'html.parser')
    container = soupy.find(class_='text')
    if "North America" in container.text:
        plant_names.append((soupy.find(class_='productName').text, key))
        
with open('data3.pkl','wb') as pkl_jar:
    pickle.dump(plant_names, pkl_jar, -1)
'''

# UNCOMMENT BELOW to print your pickle!

'''
with open('data3.pkl', 'rb') as pkl_juice:
    plants = pickle.load(pkl_juice)
    
print(plants)
'''
    
