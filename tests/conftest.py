import pytest
from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


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


@pytest.fixture(autouse=True)
def reset_category_counters():  # сброс счётчиков
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def forth_product():
    return Product(
        name="Xiaomi Redmi Note 11",
        description="024GB, Синий",
        price=31000.0,
        quantity=14
    )


@pytest.fixture
def product_dict():
    return {
        "name": "Realme 12 Pro",
        "description": "128GB, Синий цвет",
        "price": 25000.0,
        "quantity": 3
    }

@pytest.fixture
def first_smartphone():
    return Smartphone(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
        efficiency=95.5,
        model="S23 Ultra",
        memory=256,
        color="Серый"
    )

@pytest.fixture
def second_smartphone():
    return Smartphone(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
        efficiency = 98.2,
        model = "15",
        memory = 512,
        color = "Gray space"
    )

@pytest.fixture
def first_lawngrass():
    return LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый"
    )

@pytest.fixture
def second_lawngrass():
    return LawnGrass(
        name="Газонная трава 2",
        description="Выносливая трава",
        price=450.0,
        quantity=15,
        country="США",
        germination_period="5 дней",
        color="Темно-зеленый"
    )
