RATING_MAP = {
    "One": 1.0,
    "Two": 2.0,
    "Three": 3.0,
    "Four": 4.0,
    "Five": 5.0
}


def parse_rating(rating_text: str | None):
    if not rating_text:
        return None
    
    rating_text = rating_text.strip()
    
    return RATING_MAP.get(rating_text, None)