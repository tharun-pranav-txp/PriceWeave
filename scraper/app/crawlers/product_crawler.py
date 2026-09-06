import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from collections import deque

from .base import BaseCrawler


class ProductCrawler(BaseCrawler):
    
    def crawl(self, start_url: str, max_pages: int = 3):

        queue = deque([start_url])
        visited = set()
        product_urls = []

        while queue and len(visited) < max_pages:

            url = queue.popleft()

            if url in visited:
                continue

            visited.add(url)

            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            # Find individual product pages
            product_links = soup.select("article.product_pod h3 a")

            for link in product_links:

                product_url = urljoin(url, link["href"])

                if product_url not in product_urls:
                    product_urls.append(product_url)

            # Continue to the next catalogue page
            next_page = soup.select_one("li.next a")

            if next_page:
                next_url = urljoin(url, next_page["href"])

                if next_url not in visited:
                    queue.append(next_url)

        return product_urls