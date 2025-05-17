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


def test_new_product_from_dict(product_dict):
    # Очистим список продуктов перед тестом
    Product.products = []

    product = Product.new_product(product_dict)

    assert isinstance(product, Product)
    assert product.name == "Realme 12 Pro"
    assert product.description == "128GB, Синий цвет"
    assert product.price == 25000.0
    assert product.quantity == 3
    assert len(Product.products) == 1  # Новый продукт добавлен в список


def test_new_product_updates_existing(product_dict):
    # Очистим список и добавим продукт вручную
    Product.products = []
    existing_product = Product("Realme 12 Pro", "128GB, Синий цвет", 24000.0, 2)
    Product.products.append(existing_product)

    updated_product = Product.new_product(product_dict)

    # Проверим, что количество увеличилось (2 + 3)
    assert updated_product.quantity == 5

    # Проверим, что цена обновилась, потому что 25000 > 24000
    assert updated_product.price == 25000.0

    # Список продуктов не должен увеличиться
    assert len(Product.products) == 1


def test_new_product_invalid_price(product_dict):
    product_dict["price"] = "not_a_number"

    with pytest.raises(ValueError, match="Цена должна быть числом"):
        Product.new_product(product_dict)


def test_new_product_invalid_quantity(product_dict):
    product_dict["quantity"] = "five"

    with pytest.raises(ValueError, match="Количество должно быть целым числом"):
        Product.new_product(product_dict)


def test_price_zero(product_dict):
    product = Product.new_product(product_dict)

    assert product.price == 25000.0

def test_price_negative_value(forth_product, capsys):
    forth_product.price = -50.0
    out, _ = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in out
    assert forth_product.price == 31000.0  # цена не изменилась


def test_price_lower_price_yes(forth_product, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Y")
    forth_product.price = 30000.0
    assert forth_product.price == 30000.0  # цена обновлена


def test_price_lower_price_no(forth_product, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "N")
    forth_product.price = 30000.0
    assert forth_product.price == 31000.0 # цена не изменилась


def test_price_higher_price(forth_product):
    forth_product.price = 33000.0
    assert forth_product.price == 33000.0  # цена изменилась без вопросов


def test_product_str(first_product):
    assert str(first_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"


def test_product_add(first_product, second_product):
    assert first_product + second_product == 2580000.0


def test_wrong_product_add(first_product, first_category):
    with pytest.raises(TypeError) as exc_info:
        result = first_product + first_category
    assert "Невозможно сложить объекты разных типов:" in str(exc_info.value)
