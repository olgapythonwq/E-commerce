import pytest

from src.order import Order


def test_order_init(first_order):
    assert first_order.name == "Samsung Galaxy S23 Ultra"
    assert first_order.description == "256GB, Серый цвет, 200MP камера"
    assert first_order.quantity == 2


def test_order_init_with_negative_quantity(first_lawngrass):
    with pytest.raises(ValueError) as exc_info:
        Order(first_lawngrass, -5)
    assert str(exc_info.value) == "Количество должно быть положительным"


def test_order_str(first_order):
    assert str(first_order) == "Заказ: Samsung Galaxy S23 Ultra 2 шт. на общую сумму 360000.0 руб."
