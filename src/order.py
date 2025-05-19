from src.base_entity import BaseEntity
from src.product import Product


class Order(BaseEntity):
    """Класс для описания заказов"""
    product: Product
    quantity: int
    total_price: float

    def __init__(self, product: Product, quantity: int) -> None:
        """Инициализация экземпляра заказа."""
        self.name = product.name
        self.description = product.description
        super().__init__()

        if quantity <= 0:
            raise ValueError("Количество должно быть положительным")
        self.product = product
        self.quantity = quantity
        self.total_price = self.product.price * self.quantity

    def __str__(self) -> str:
        """Функция, предоставляющая строковое отображение заказа, количество продукта и общей стоимости"""
        return f"Заказ: {self.name} {self.quantity} шт. на общую сумму {self.total_price} руб."
