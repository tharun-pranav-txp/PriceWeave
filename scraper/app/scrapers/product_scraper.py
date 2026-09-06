from urllib.parse import urlparse

from .retailers.books_to_scrape import BooksToScrapeScraper


class ProductScraper:
    
    def __init__(self):
        self.retailer_scrapers = {
            "books.toscrape.com": BooksToScrapeScraper(),
        }
        
    def scrape(self, url: str):
        
        hostname = urlparse(url).netloc
        
        for domain, scraper in self.retailer_scrapers.items():
            
            if hostname == domain or hostname.endswith("." + domain):
                return scraper.scrape(url)
            
        return None