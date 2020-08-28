import requests
from bs4 import BeautifulSoup

def search(key):
  page = requests.get('https://search.yahoo.com/search?q='+key).text
  soup = BeautifulSoup(page, 'html.parser')
  restags = soup.find_all('span')
  restag = restags[-5]
  res1 = restag.get_text().split('span')
  res2 = ''.join(res1)
  res3 = res2.split('</span>')
  finalresult = ''.join(res3)
  return finalresult