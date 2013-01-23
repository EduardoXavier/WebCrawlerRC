#! /usr/bin/env python
#coding: utf-8
#Edmundo Silveira - Eduardo Xavier
#Redes de Computadores 1 - UFPel
#2012/2

import threading
from BeautifulSoup import BeautifulSoup
from functools import partial
import urllib2
import re
import sys

#Função para o rastreamento
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
		
#Main	
profundidade = int(sys.argv[2])  #Nivel de profundidade passado na linha de comando.  
url = sys.argv[1] #URL passada na linha de comando.
threads = [] #Lista contendo as threads.
#Utiliza 4 threads e faz o join.
for n in range(4):
    thread = threading.Thread(target=partial(meucrawler,url,profundidade))
    thread.start()
    print "########### Thread Num= %d ##########" % (n+1)
    threads.append(thread)
print "Carregando..."
for thread in threads:
    thread.join()       

