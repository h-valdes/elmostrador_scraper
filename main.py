#pip3 install requests beautifulsoup4
from bs4 import BeautifulSoup
import requests
page_link ='http://www.elmostrador.cl/claves/sebastian-pinera/'

pinera=[]

#find where the Error 404 is located
def page_counter(link):
	n=520
	while True:
		new_link=link+"page/"+str(n)+"/"
		page_response = requests.get(new_link, timeout=5)	
		page_content = BeautifulSoup(page_response.content, "html.parser")
		title=page_content.title
		if title.text=="El Mostrador - Página no encontrada":
			print("Error 404 in page: "+str(n))
			return n
		else:
			print(n)
			n=n+1
	

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

def iterator():
	for i in range(1,5):
		page_link='http://www.elmostrador.cl/claves/sebastian-pinera/page/'+str(i)+'/'
		pinera_scraper(articles_selector(page_link))
		for i in pinera_scraper(articles_selector(page_link)):
			pinera.append(i)
	print(pinera)

#iterator()
page_counter(page_link)
