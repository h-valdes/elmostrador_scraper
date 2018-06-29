#pip3 install requests beautifulsoup4
from bs4 import BeautifulSoup
import requests
import json

pinera=[]

#find where the Error 404 is located
def page_counter(link):
	n=1
	while True:
		new_link=link+"page/"+str(n)+"/"
		page_response = requests.get(new_link, timeout=5)	
		page_content = BeautifulSoup(page_response.content, "html.parser")
		title=page_content.title
		if title.text=="El Mostrador - Página no encontrada":
			print("Error 404 in page: "+str(n))
			return n-1
		else:
			print(n)
			n=n+1

def articles_selector(link):
	articles=[]
	page_response = requests.get(link, timeout=5)
	page_content = BeautifulSoup(page_response.content, "html.parser")
	all_articles = page_content.find_all('article')
	for i in all_articles:
		if i.find(class_="fecha"):
			articles.append(scraper(i))
	return articles

def scraper(article):
	page_articles=[]	
	components={}
	date=article.find("p").text.split("|")[0]
	title=article.find('a').text
	author=article.find_all('p')[1].text
	link=article.find('a').get('href')
	components['date']=date
	components['title']=title
	components['author']=author
	components['link']=link
	page_articles.append(components)
	return page_articles

def first_iterator():	
	tag='sebastian-pinera'
	pages=page_counter('http://www.elmostrador.cl/claves/sebastian-pinera/')
	for i in reversed(range(520,pages+1)):
		page_link='http://www.elmostrador.cl/claves/'+tag+'/page/'+str(i)+'/'
		print(articles_selector(page_link))


