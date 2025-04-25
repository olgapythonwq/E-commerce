from src.category import Category


def test_category_init(first_category, first_product, second_product):  # передаём fixtures
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство не только коммуникации, но и дополнительных функций"
    assert first_category.products == [first_product, second_product]
    assert Category.category_count == 1
    assert Category.product_count == 2
