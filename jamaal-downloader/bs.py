import requests
import os
import string
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import json
import lxml
import re
# soup = BeautifulSoup(html_doc, 'html.parser')
headers = {'User-Agent': 'Mozilla/5.0'}
path = os.getcwd() + '/mp4/'
if not os.path.exists(path):
    os.makedirs(path)
url = 'https://muslimcentral.com/audio/jamal-zarabozo/'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urlopen(req)
# req = requests.get(url, headers)
# response = urlopen(req,  data=bytes(json.dumps(headers), encoding="utf-8"))
soup = BeautifulSoup(response.read(), 'lxml')
script_tags  = soup.find_all("script")
pattern = re.compile(r"\[(.*)\]")
print(script_tags[4].string)
# for script in script_tags:
#     print("trying")
#     print(script.string)
#     if (pattern.match(str(script.string))):
#         print('here')
#         data = pattern.match(script.string)
#         stock = json.loads(data.groups()[0])
#         print(stock)
# print(data)
# p = re.compile('const data = (.*?);')
# print(p)
# print(ss)
# soup = BeautifulSoup(req.read(), 'lxml')

# print(soup.prettify())