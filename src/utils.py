import json
import os
from pprint import pprint
from typing import Any

from src.category import Category
from src.product import Product


def read_json(path: str) -> Any:
    """Функция, загружающая данные из json-файла"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: dict) -> list:
    """Функция, создающая экземпляры классов из данных из json-файла"""
    categories = []
    for category in data:  # category - это словарь, который нужно преобразовать в экземпляр класса
        products = []
        for product in category["products"]:
            products.append(Product(**product))  # добавляем экземпляр класса с распаковкой **
        category["products"] = products  # вместо словарей будет лежать список экземпляров
        categories.append(Category(**category))

    return categories


if __name__ == '__main__':
    raw_data = read_json("../data/products.json")
    pprint(raw_data)
    categories_data = create_objects_from_json(raw_data)
    print(categories_data)
    print(categories_data[0].name)
    print(categories_data[0].products)
