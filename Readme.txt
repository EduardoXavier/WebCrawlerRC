#Edmundo Silveira - Eduardo Xavier
#Redes de Computadores 1 - UFPel
#2012/2
Método meucrawler:
	-Recebe como parâmetro a url e a profundidade desejada,no momento da chamada do arquivo pela linha de comando.
	-Utiliza a biblioteca Beautiful Soup para o acesso de links.
Sobre as Threads:
	-Utiliza uma lista contendo as threads.	
	-Utiliza 4 threads e no final faz o join das mesmas.

Para rodar o programa:
	-Instalar a biblioteca BeautifulSoup:

		python setup.py install
	-Digitar no terminal,após acessar a pasta do arquivo:  - chmod a+x spider.py
			       				       - ./spider.py URL Profundidade
									Ex: ./spider.py http://www.globo.com 20	
			       				       - Ou python spider.py URL Profundidade
									Ex: python spider.py http://www.globo.com 20	

BUG: Cada Thread esta buscando sempre os mesmos links.:/

Testes Realizados:
 1 )
edmundo@edmundo-Vostro-3550:~/Downloads/WebCrawler-v1$	python spider.py http://www.globo.com 6
########### Thread Num= 1 ##########
########### Thread Num= 2 ##########
########### Thread Num= 3 ##########
########### Thread Num= 4 ##########
Carregando...
http://ads.globo.com/RealMedia/ads/click_nx.ads/globo.com/globo.com/home/@x19
/
http://g1.globo.com/
http://g1.globo.com/
None
http://g1.globo.com/brasil/
http://ads.globo.com/RealMedia/ads/click_nx.ads/globo.com/globo.com/home/@x19
/
http://g1.globo.com/
http://g1.globo.com/
None
http://g1.globo.com/brasil/
http://ads.globo.com/RealMedia/ads/click_nx.ads/globo.com/globo.com/home/@x19
/
http://g1.globo.com/
http://g1.globo.com/
None
http://g1.globo.com/brasil/
http://ads.globo.com/RealMedia/ads/click_nx.ads/globo.com/globo.com/home/@x19
/
http://g1.globo.com/
http://g1.globo.com/
None
http://g1.globo.com/brasil/
===================================================
 2 )
edmundo@edmundo-Vostro-3550:~/Downloads/WebCrawler-v1$ ./spider.py http://www.fox.com 4
########### Thread Num= 1 ##########
########### Thread Num= 2 ##########
########### Thread Num= 3 ##########
########### Thread Num= 4 ##########
Carregando...
/
/shows/
http://www.fox.com/americandad
http://americanidol.com
/
/shows/
http://www.fox.com/americandad
http://americanidol.com
/
/shows/
http://www.fox.com/americandad
http://americanidol.com
/
/shows/
http://www.fox.com/americandad
http://americanidol.com




