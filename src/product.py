class Product:
    """Класс для описания продуктов"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        if price <= 0:
            raise ValueError("Цена не может быть отрицательной или равной нулю")
        self.price = price
        if quantity <= 0:
            raise ValueError("Количество не может быть отрицательным или равным нулю")
        self.quantity = quantity
