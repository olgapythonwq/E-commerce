import pytest

from src.category import Category, ProductIterator


def test_category_init(first_category, first_product, second_product):  # передаём fixtures из conftest.py
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство не только коммуникации, но и дополнительных функций"
    assert "Samsung" in first_category.products
    assert "Iphone" in first_category.products
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_add_product(first_category, forth_product):  # передаём fixtures из conftest.py
    assert Category.product_count == 2
    first_category.add_product(forth_product)

    assert "Xiaomi" in first_category.products
    assert Category.product_count == 3


def test_add_product_incorrect_product(first_category):
    assert Category.product_count == 2
    with pytest.raises(TypeError, match="Невозможно добавить указанный продукт в категорию"):
        first_category.add_product(["name", "Realme 12 Pro", "description",
                                    "128GB, Синий цвет", "price", 25000.0, "quantity", 3])
    assert Category.product_count == 2


def test_product_str(first_category):
    assert str(first_category) == "Смартфоны, количество продуктов: 13 шт."


def test_product_iterator(first_category, first_product, second_product):
    iterator = ProductIterator(first_category)

    products = list(iterator)
    assert products == [first_product, second_product]
