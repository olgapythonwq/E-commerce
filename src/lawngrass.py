from typing import Any

from src.product import Product


class LawnGrass(Product):

    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: str,
                 color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: Any) -> float:
        if type(other) is LawnGrass:
            full_cost = self.price * self.quantity + other.price * other.quantity
            return full_cost
        raise TypeError(f"Невозможно сложить объекты разных типов: {type(self)} и {type(other)}")
