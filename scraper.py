import urllib
class Scraper():
    def __init__(self, url):
        self.url = url
        
    def get_page(self, page_num):
        f = urllib.urlopen(self.url)
        data = f.read()
        f.close()
        return data

    def procesa_proyectos(self):
	x = [1,2,3,4,5]     
	return x
	
	

