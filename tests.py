import unittest

from scraper import Scraper

class TestScraper(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_page(self):
        scraper = Scraper()
        data = scraper.get_page(1)
        assert data != ""
        print data
        assert data.startswith('<html>')
    
    
