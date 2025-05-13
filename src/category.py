from typing import List, Optional

from src.product import Product


class Category:
    """Класс для описания категорий товаров"""
    # Атрибуты экземпляра:
    name: str
    description: str
    __products: list[Product]

    # Атрибуты класса:
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        """Инициализация категории"""
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        """Функция, осуществляющая добавление продукта в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Невозможно добавить указанный продукт в категорию")

    @property
    def products(self) -> str:
        """Функция с методом геттера для получения списка продуктов"""
        products_list = ""
        for product in self.__products:
            products_list += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_list
