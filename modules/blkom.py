from lxml import html

import requests


site = "https://animeblkom.net/anime-list?sort_by=rate&page="

def animeList(page=1):
  page = requests.get(site+str(page))
  tree = html.fromstring(page.text)
  animes = tree.xpath(
      '//div[@class="name"]/a/@href')
  return animes
def animeData(url):
  page = requests.get(url)
  tree = html.fromstring(page.text)
  name = tree.xpath('//div[@class="name col-xs-12"]/span/h1/text()')
  story = tree.xpath(
      '//div[@class="story"]/p/text()')
  return name,story
  


