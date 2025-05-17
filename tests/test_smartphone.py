import pytest

from src.smartphone import Smartphone


def test_smartphone_init(first_smartphone):
    assert first_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert first_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert first_smartphone.price == 180000.0
    assert first_smartphone.quantity == 5
    assert first_smartphone.efficiency == 95.5
    assert first_smartphone.model == "S23 Ultra"
    assert first_smartphone.memory == 256
    assert first_smartphone.color == "Серый"


def test_smartphone_add(first_smartphone, second_smartphone):
    assert first_smartphone + second_smartphone == 2580000.0

def test_wrong_product_add(first_smartphone, first_lawngrass):
    with pytest.raises(TypeError) as exc_info:
        result = first_smartphone + first_lawngrass
    assert "Невозможно сложить объекты разных типов:" in str(exc_info.value)
