import argparse
import scraper

parser=argparse.ArgumentParser()
parser.add_argument('-f','--first_iterator',help='First time to iterate over the whole page.',action="store_true")
parser.add_argument('-c','--counter',help='Count how many pages has the target.',action="store_true")
parser.add_argument('-m','--max_id',help='Show the biggest ID in JSON File.',action="store_true")
parser.add_argument('-u','--update',help='Update the current file.',action="store_true")
args=parser.parse_args()
if args.first_iterator:
	scraper.first_iterator()
elif args.counter:
	scraper.page_counter('http://www.elmostrador.cl/claves/sebastian-pinera/')
elif args.max_id:
	scraper.max_id()
elif args.update:
	scraper.update()
