from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    name: str
    email: str
    age: Optional[int] = None
    
    def __post_init__(self):
        """Custom validation after initialization."""
        if "@" not in self.email:
            raise ValueError("Invalid email")


@dataclass
class Product:
    name: str
    price: float
    
    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")


@dataclass
class Order:
    user: User
    product: Product
    quantity: int = 1
