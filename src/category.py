from typing import Iterator, List, Optional

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

    def __str__(self) -> str:
        """Функция, предоставляющая строковое отображение категории и общего количества продуктов"""
        product_count = 0
        for product in self.__products:
            product_count += product.quantity
        return f'{self.name}, количество продуктов: {product_count} шт.'

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
            products_list += f"{str(product)}\n"
        return products_list

    @property
    def products_in_list(self) -> list[Product]:
        """Функция-геттер, которая возвращает список продуктов, как объектов класса"""
        return self.__products


class ProductIterator (Iterator):
    """Вспомогательный класс для перебора продуктов в заданной категории"""

    def __init__(self, category: Category) -> None:
        """Инициализирует итератор продуктами из переданной категории.
        :param category: Объект категории, содержащий список продуктов."""
        self.__products = category.products_in_list  # Список продуктов из категории
        self.current_index = 0

    def __iter__(self) -> 'ProductIterator':
        """Возвращает сам итератор."""
        self.current_index = 0
        return self

    def __next__(self) -> Product:
        """Возвращает следующий продукт из списка. Если достигнут конец — возбуждает исключение StopIteration."""
        if self.current_index < len(self.__products):
            result = self.__products[self.current_index]
            self.current_index += 1
            return result
        else:
            raise StopIteration
