import re

import requests
from bs4 import BeautifulSoup

from ..base import BaseScraper
from app.models.product import Product
from app.parsers.price_parser import parse_price
from app.parsers.rating_parser import parse_rating


class BooksToScrapeScraper(BaseScraper):
    
    def clean_description(self, text: str):
        text = re.sub(r"\s+", " ", text).strip()
        
        anchor = text[:60]
        second_start = text.find(anchor, 60)
        
        if second_start != -1:
            text = text[second_start:]
            
        text = re.sub(r"\s*\.\.\.more\s*$", "", text, flags=re.IGNORECASE)
            
        text = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)
            
        return text

    def scrape(self, url: str):
        res = requests.get(url)
        res.encoding = res.apparent_encoding
        
        if res.status_code != 200:
            return None

        soup = BeautifulSoup(res.text, "html.parser")
        
        product = soup.select_one("article.product_page")
        
        if not product:
            return None

        title = product.select_one("div.product_main h1").get_text(strip=True)
        
        description_element = product.select_one("#product_description + p")

        description = (
            self.clean_description(
                description_element.get_text(" ", strip=True)
            )
            if description_element
            else None
        )

        price = product.select_one(".price_color").get_text(strip=True)
        price, currency = parse_price(price)

        rating = product.select_one("p.star-rating")["class"][1]
        rating = parse_rating(rating)
            
        return Product(
            title=title,
            description=description,
            price=price,
            currency=currency,
            rating=rating,
            url=url
        )