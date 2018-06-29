import argparse
import scraper

parser=argparse.ArgumentParser()
parser.add_argument('-i','--iterator',help='Iterate over the whole page.',action="store_true")
parser.add_argument('-c','--counter',help='Count how many pages are for the target.',action="store_true")
args=parser.parse_args()
if args.iterator:
	scraper.first_iterator()
if args.counter:
	page_link ='http://www.elmostrador.cl/claves/sebastian-pinera/'
	scraper.page_counter(page_link)
