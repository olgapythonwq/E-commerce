from typing import Any

from src.product import Product


class Smartphone(Product):

    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: float, model: str,
                 memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: Any) -> float:
        if type(other) is Smartphone:
            full_cost = self.price * self.quantity + other.price * other.quantity
            return full_cost
        raise TypeError(f"Невозможно сложить объекты разных типов: {type(self)} и {type(other)}")
