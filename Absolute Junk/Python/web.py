import requests
from bs4 import BeautifulSoup

# URL = 'https://www.bbc.com'
URL='https://www.bbc.com/news/world-us-canada-56572472'

r = requests.get(URL)

soup = BeautifulSoup(r.text, 'html.parser')

first = soup.find('a', {'class':'media__link'})

print(first.text.strip())