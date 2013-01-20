import threading
from BeautifulSoup import BeautifulSoup

import urllib2
import re
import sys

def meucrawler(page,grau):
	contador=1
	paginaweb = urllib2.urlopen(page)
	soup = BeautifulSoup(paginaweb)
	if contador==grau+1:
		SystemExit
	else:
		for link in soup.findAll("a",recursive=True,limit=grau):				
		 		print link.get('href')  		 		
				
		contador=contador+1			
profundidade = int(sys.argv[2]) 
url = sys.argv[1] 
