import re


CURRENCY_SYMBOLS = {
    "$": "USD",
    "€": "EUR",
    "£": "GBP",
    "¥": "JPY",
    "₹": "INR",
    "₩": "KRW",
    "₽": "RUB",
    "₺": "TRY",
    "₴": "UAH",
    "₦": "NGN",
    "₱": "PHP",
    "₪": "ILS",
    "₫": "VND",
    "₡": "CRC",
    "₲": "PYG",
    "₵": "GHS",
}


def parse_price(price_text: str):
    if not price_text:
        return None, None
    
    price_text = price_text.strip()
    
    currency = None
    
    for symbol, code in CURRENCY_SYMBOLS.items():
        if symbol in price_text:
            currency = code
            break
        
    number = re.sub(r"[^\d.,]", "", price_text)
    
    if not number:
        return None, currency

    number = number.replace(",", "")
    
    try:
        price = float(number)
    except ValueError:
        return None, currency
    
    return price, currency