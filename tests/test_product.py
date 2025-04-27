import pytest

from src.product import Product


def test_product_init(first_product):
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5


def test_product_init_with_negative_price():
    with pytest.raises(ValueError) as exc_info:
        Product("Bad Product", "This is a bad product", -1.11, 3)
    assert str(exc_info.value) == "Цена не может быть отрицательной или равной нулю"


def test_product_init_with_negative_quantity():
    with pytest.raises(ValueError) as exc_info:
        Product("Very bad Product", "This is a very bad product", 10, -5)
    assert str(exc_info.value) == "Количество не может быть отрицательным или равным нулю"
