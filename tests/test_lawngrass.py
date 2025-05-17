import pytest

from src.lawngrass import LawnGrass


def test_lawngrass_init(first_lawngrass):
    assert first_lawngrass.name == "Газонная трава"
    assert first_lawngrass.description == "Элитная трава для газона"
    assert first_lawngrass.price == 500.0
    assert first_lawngrass.quantity == 20
    assert first_lawngrass.country == "Россия"
    assert first_lawngrass.germination_period == "7 дней"
    assert first_lawngrass.color == "Зеленый"


def test_lawngrass_add(first_lawngrass, second_lawngrass):
    assert first_lawngrass + second_lawngrass == 16750.0

def test_wrong_product_add(first_lawngrass, second_smartphone):
    with pytest.raises(TypeError) as exc_info:
        result = first_lawngrass + second_smartphone
    assert "Невозможно сложить объекты разных типов:" in str(exc_info.value)

