import urllib
class Scraper():
    def __init__(self):
        self.url = "http://www2.congreso.gob.pe/Sicr/TraDocEstProc/CLProLey2011.nsf/PAporfecha?OpenView&Start=%i%&Count=5&ExpandView"
        
    def get_page(self, page_num):
        f = urllib.urlopen(self.url)
        data = f.read()
        f.close()
        return data
