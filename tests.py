import unittest

from scraper import Scraper

class TestScraper(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_page(self):
	scraper = Scraper("htmltests/p1_5.html")
        proyectos = scraper.procesa_proyectos()
	assert 5, proyectos.__len__()
    
    
