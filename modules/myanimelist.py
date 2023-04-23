from lxml import html

import requests
import random


site = "https://myanimelist.net/character.php?limit="


def charactersList(limit=0):
  page = requests.get(site+str(limit))
  tree = html.fromstring(page.text)
  character = tree.xpath('//tr[@class="ranking-list"]/td/a/@href')
  return character

def characterData(url):
  page = requests.get(url)
  tree = html.fromstring(page.text)
  names = tree.xpath('//div[@class="h1 edit-info"]/div/h1[@class="title-name h1_bold_none"]/strong/text()')
  
   
  image_url = tree.xpath('//td[@class="borderClass"]/div[@style="text-align: center;"]/a/img/@data-src')
  return names , image_url
   
