import requests
import os
import string
from bs4 import BeautifulSoup

class HeartWork:
  def __init__(self, base_url, episode_count):
    self.base_url = base_url
    self.episode_count = episode_count
    self.list_of_urls = []
    idx = base_url.rfind('/') + 1
    self.title = base_url[idx:]
  
  def __generate_urls(self):
    print('Generating URLs')
    idx = self.base_url.find('/audio/')
    for i in range(1, self.episode_count + 1):
      str_idx = str(i)
      link = self.base_url[:80] + str_idx + self.base_url[81:]
      episode_title = self.title[:17] + str_idx + self.title[18:]
      self.list_of_urls.append([link, episode_title])
    print('URLs generated')
    
  
  def __download_files(self):
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

    print('Downloading files... Please wait')

    path = os.getcwd() + '/heartwork/'
    if not os.path.exists(path):
      os.makedirs(path)
    for i, mix in enumerate(self.list_of_urls):
      print('Downloading file:', mix[0])
      req = requests.get(mix[0], headers)

      with open(os.path.join(path, mix[1]), 'wb') as f:
        f.write(req.content)
    print('Downloads complete.')

  def begin(self):
    self.__generate_urls()
    self.__download_files()
