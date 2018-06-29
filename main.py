import argparse
import scraper

parser=argparse.ArgumentParser()
parser.add_argument('-i','--iterator',help='First time to iterate over the whole page.',action="store_true")
parser.add_argument('-c','--counter',help='Count how many pages has the target.',action="store_true")
args=parser.parse_args()
if args.iterator:
	scraper.first_iterator()
if args.counter:
	scraper.page_counter('http://www.elmostrador.cl/claves/sebastian-pinera/')
