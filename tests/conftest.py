import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def first_product():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
    )


@pytest.fixture
def second_product():
    return Product(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8
    )


@pytest.fixture
def third_product():
    return Product(
        name="55\" QLED 4K",
        description="Фоновая подсветка",
        price=123000.0,
        quantity=7
    )


@pytest.fixture
def first_category(first_product, second_product):
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и дополнительных функций",
        products=[first_product, second_product]
    )


@pytest.fixture
def second_category(third_product):
    return Category(
        name="Телевизоры",
        description="Современный телевизор",
        products=[third_product]
    )


@pytest.fixture
def json_for_test():
    return [
  {
    "name": "Смартфоны",
    "description": "Разнообразные смартфоны",
    "products": [
      {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      },
      {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
      }
    ]
  },
  {
    "name": "Телевизоры",
    "description": "Современный телевизор",
    "products": [
      {
        "name": "55\" QLED 4K",
        "description": "Фоновая подсветка",
        "price": 123000.0,
        "quantity": 7
      }
    ]
  }
]