#pip3 install requests beautifulsoup4
from bs4 import BeautifulSoup
import requests
page_link ='http://www.elmostrador.cl/claves/sebastian-pinera/'

pinera=[]

def articles_selector(link):
	page_response = requests.get(link, timeout=5)
	page_content = BeautifulSoup(page_response.content, "html.parser")
	articles = page_content.find_all('article',limit=10)
	return articles
#takes a list for of articles

def pinera_scraper(articles):
	page_articles=[]	
	components={}
	for i in articles:
		date=i.find("p").text.split("|")[0]
		titel=i.find('a').text
		autor=i.find_all('p')[1].text
		link=i.find('a').get('href')
		components['date']=date
		components['titel']=titel
		components['autor']=autor
		components['link']=link
		page_articles.append(components)
	return page_articles

for i in range(1,50):
	page_link='http://www.elmostrador.cl/claves/sebastian-pinera/page/'+str(i)+'/'
	pinera_scraper(articles_selector(page_link))
	for i in pinera_scraper(articles_selector(page_link)):
		pinera.append(i)
print(pinera)
