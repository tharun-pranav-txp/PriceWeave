from dataclasses import dataclass


@dataclass
class Product:
    title: str
    description: str | None
    price: float | None
    currency: str | None
    rating: str | None
    url: str