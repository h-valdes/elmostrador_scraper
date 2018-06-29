#pip3 install requests beautifulsoup4
from bs4 import BeautifulSoup
import requests
import json
import os

#find where the Error 404 is located
def page_counter(link):
	n=1
	while True:
		new_link=link+"page/"+str(n)+"/"
		page_response = requests.get(new_link, timeout=10)	
		page_content = BeautifulSoup(page_response.content, "html.parser")
		title=page_content.title
		if title.text=="El Mostrador - Página no encontrada":
			print("Error 404 in page: "+str(n))
			return n-1
		else:
			print(n)
			n=n+1

def max_id():
	data={}
	with open('data.txt', encoding='utf-8') as outfile:
		data=json.load(outfile)	
	ids=list(map(int,data.keys()))
	biggest_id=max(ids)
	print(biggest_id)

def articles_selector(link):
	articles=[]
	page_response = requests.get(link, timeout=5)
	page_content = BeautifulSoup(page_response.content, "html.parser")
	all_articles = page_content.find_all('article')
	for i in all_articles:
		if i.find(class_="fecha"):
			scraper(i)

def scraper(article):
	data={}
	date="a"
	if os.path.isfile('data.txt'):
		with open('data.txt', encoding='utf-8') as outfile:
			data=json.load(outfile)
		ids=list(map(int, data.keys()))
		id_number=str(max(ids)+1)			
	else:
		id_number="1"
	components={}
	date=article.find("p").text.split("|")[0]
	title=article.find('a').text
	author=article.find_all('p')[1].text
	link=article.find('a').get('href')
	components['date']=date
	components['title']=title
	components['author']=author
	components['link']=link	
	for i in data.keys():
		if data[i]['title']==title:
			return			
	data[id_number]=components
	with open('data.txt','w', encoding='utf-8') as outfile:
		json.dump(data,outfile,ensure_ascii=False,sort_keys=True, indent=4)

def first_iterator():	
	tag='sebastian-pinera'
	pages=page_counter('http://www.elmostrador.cl/claves/sebastian-pinera/')
	for i in reversed(range(1,pages+1)):
		page_link='http://www.elmostrador.cl/claves/'+tag+'/page/'+str(i)+'/'
		articles_selector(page_link)

