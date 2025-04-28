from typing import Any


class Product:
    """Класс для описания продуктов"""
    # Атрибуты экземпляра:
    name: str
    description: str
    __price: float
    quantity: int
    # Атрибуты класса:
    products: list = []

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализация экземпляра продукта."""
        self.name = name
        self.description = description

        if price <= 0:
            raise ValueError("Цена не может быть отрицательной или равной нулю")
        self.__price = price

        if quantity <= 0:
            raise ValueError("Количество не может быть отрицательным или равным нулю")
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_dict: dict) -> Any:
        """Класс-метод создающий новый продукт на основе словаря"""
        # Проверяем и приводим типы данных в словаре перед использованием
        name = str(product_dict.get("name", ""))  # второй аргумент .get() — это значение по умолчанию
        description = str(product_dict.get("description", ""))  # Если ключа "name" нет, то вернется пустая строка ""
        price_raw = product_dict.get("price")
        quantity_raw = product_dict.get("quantity")

        if not isinstance(price_raw, (int, float)):
            raise ValueError("Цена должна быть числом")
        if not isinstance(quantity_raw, int):
            raise ValueError("Количество должно быть целым числом")

        price = float(price_raw)
        quantity = int(quantity_raw)

        for product in cls.products:  # Проверка есть ли продукт в списке продуктов
            if product.name == name:  # Если продукт существует, то обновим количество и цену
                product.quantity += quantity
                if product.price < price:  # Если цена сущ-го продукта меньше, то обновим цену
                    product.price = price
                return product
        # Если продукта не существует, то создадим его
        new_product = cls(name, description, price, quantity)
        cls.products.append(new_product)
        return new_product

    @property
    def price(self) -> float:
        """Функция с методом геттер, возвращающая приватный атрибут цена"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Функция с методом сеттер, для установки новой цены"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            print(f"Вы уверены, что хотите снизить цену с {self.__price} до {new_price}?")
            user_answer = input("Введите Y для подтверждения или N для сохранения текущей цены. (Y/N): ")
            if user_answer.lower() == "y":
                self.__price = new_price
        else:
            self.__price = new_price
