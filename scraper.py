#pip3 install requests beautifulsoup4
from bs4 import BeautifulSoup
import requests
import json
import os
import sys
class Elmostrador_scraper():
	def __init__(self,tag):
		self.tag=tag

	#find where the Error 404 is located
	def page_counter(self,link):
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

	def max_id(self):
		data={}
		with open(self.tag+'.txt', encoding='utf-8') as outfile:
			data=json.load(outfile)	
		ids=list(map(int,data.keys()))
		biggest_id=max(ids)
		print(biggest_id)
		return biggest_id

	def articles_selector(self,link):
		articles=[]
		flag=True
		page_response = requests.get(link, timeout=5)
		page_content = BeautifulSoup(page_response.content, "html.parser")
		all_articles = page_content.find_all('article')
		for i in all_articles:
			if i.find(class_="fecha"):
				a,b=scraper(i)
				data_dumper(a,b)
		return flag

	def scraper(self,article):
		data={}
		date="a"
		if os.path.isfile(self.tag+'.txt'):
			with open('data.txt', encoding='utf-8') as outfile:
				data=json.load(outfile)	
			ids=list(map(int,data.keys()))
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
				#return
				sys.exit()
		return id_number,components	

	def data_dumper(self,id_number,dict_article):	
		data={}
		with open(self.tag+'.txt', encoding='utf-8') as outfile:
				data=json.load(outfile)
		data[id_number]=dict_article
		with open(self.tag+'.txt','w', encoding='utf-8') as outfile:
			json.dump(data,outfile,ensure_ascii=False,sort_keys=True, indent=4)

	def update(self):
		page_number=1
		while True:
			page_link='http://www.elmostrador.cl/claves/'+self.tag+'/page/'+str(page_number)+'/'
			articles_selector(page_link)	

	def first_iterator(self):	
		pages=self.page_counter('http://www.elmostrador.cl/claves/'+self.tag+'/')
		for i in reversed(range(1,3+1)):
			page_link='http://www.elmostrador.cl/claves/'+self.tag+'/page/'+str(i)+'/'
			articles_selector(page_link)

