import requests
from bs4 import BeautifulSoup


headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})


# spidering technique to grab the links
base_url = 'https://www.fictionpress.com/s/2961893/1/Mother-of-Learning'





req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

html_input = soup.find_all('p')


