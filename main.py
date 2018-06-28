import scraper
import tui

def main():
	menu = {'title' : 'El Mostrador Scraper (Test for tag: "sebastian-pinera")',
		    'type' : 'menu',
		    'subtitle' : 'Select the action: '}

	option_1 = {'title' : 'First Iterator',
		        'type' : 'function',
		        'function' : 'first_iterator'}

	option_2 = {'title' : 'Counter of pages',
		        'type' : 'function',
		        'function' : 'page_counter'}

	menu['options'] = [option_1,option_2]

	m = tui.CursesMenu(menu)
	selected_action = m.display()
	if selected_action['type']!='exitmenu':
		if selected_action['type']=='function':
			if selected_action['function']=='first_iterator':
				scraper.first_iterator()
			elif selected_action['function']=='page_counter':
				page_link ='http://www.elmostrador.cl/claves/sebastian-pinera/'
				scraper.page_counter(page_link)
main()
