# from app.crawlers.product_crawler import ProductCrawler
# from app.scrapers.product_scraper import ProductScraper


# start_url = "https://books.toscrape.com/"

# crawler = ProductCrawler()
# scraper = ProductScraper()

# pages = crawler.crawl(start_url, max_pages=3)

# for page in pages:
#     products = scraper.scrape(page)

#     print(f"\nPage: {page}")
    
#     for product in products:
#         print(product)




from app.crawlers.product_crawler import ProductCrawler
from app.scrapers.product_scraper import ProductScraper

start_url = "https://books.toscrape.com/"

crawler = ProductCrawler()
scraper = ProductScraper()

product_urls = crawler.crawl(start_url, max_pages=1)

print(f"Found {len(product_urls)} product URLs.")

for url in product_urls:
    product = scraper.scrape(url)

    if product:
        print(product)
    else:
        print(f"Failed to scrape product at {url}")