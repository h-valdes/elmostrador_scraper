import scraper
import tui

def main():
	menu = {'title' : 'El Mostrador Scraper',
		    'type' : 'menu',
		    'subtitle' : 'Select the action: '}

	option_1 = {'title' : 'First Iterator',
		        'type' : 'function',
		        'function' : 'count'}

	menu['options'] = [option_1]

	m = tui.CursesMenu(menu)
	selected_action = m.display()
	if selected_action['type']!='exitmenu':
		if selected_action['type']=='function':
			if selected_action['function']=='count':
				scraper.first_iterator()
main()
