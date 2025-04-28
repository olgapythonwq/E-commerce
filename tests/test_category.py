from src.category import Category


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
