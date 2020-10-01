import verify

try: 
 import requests
 from bs4 import BeautifulSoup
except ImportError:
  import os
  os.system('pip install bs4')
  os.system('pip install requests')
  import requests
  from bs4 import BeautifulSoup  


def search(key):#get = 'list'):
  page = requests.get('https://search.yahoo.com/search?q='+key).text
  soup = BeautifulSoup(page, 'html.parser')
  results = []
  for i in [-1,-2,-3,-4,-5,-6,-7,-8]:
   restags = soup.find_all('span')
   restag = restags[i]
   res1 = restag.get_text().split('span')
   res2 = ''.join(res1)
   res3 = res2.split('</span>')
   res4 = ''.join(res3)
   results.insert(0,res4)
  bestresult = max(results,key=str)
  return bestresult

def searchlist(key):
  page = requests.get('https://search.yahoo.com/search?q='+key).text
  soup = BeautifulSoup(page, 'html.parser')
  results = []
  for i in [-1,-2,-3,-4,-5,-6,-7,-8]:
   restags = soup.find_all('span')
   restag = restags[i]
   res1 = restag.get_text().split('span')
   res2 = ''.join(res1)
   res3 = res2.split('</span>')
   res4 = ''.join(res3)
   results.insert(0,res4)
  return results

#EM DESIVOLVIMENTO!
def searchuseful(key):
 x = searchlist(key)
 for item in x:
  y = verify.isuse(item)
  if(y == True):
   break
   return y
print(searchuseful('cm'))