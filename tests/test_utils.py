import json
from unittest.mock import mock_open, patch

from src.utils import create_objects_from_json, read_json


def test_read_json():
    # словарь, который мы ожидаем получить от функции read_json
    mock_data = {"key": "value"}
    # создаём поддельный файл
    mock_file = mock_open(read_data=json.dumps(mock_data))
    # подменяем открытие файла и путь
    with patch("builtins.open", mock_file), patch("os.path.abspath", return_value="mocked_path.json"):
        # У функции read_json м.б. любой аргумент т.к. abspath и open замоканы.
        # Внутри read_json всё равно вызовется open("mocked_path.json").
        result = read_json("any_path.json")
        assert result == mock_data


def test_create_objects_from_json(json_for_test):
    # Вызов функции
    categories = create_objects_from_json(json_for_test)

    # Проверка, что количество категорий соответствует ожидаемому
    assert len(categories) == 2

    # Проверка первой категории
    assert categories[0].name == "Смартфоны"
    assert categories[0].description == "Разнообразные смартфоны"

    # Проверка второй категории
    assert categories[1].name == "Телевизоры"
    assert categories[1].description == "Современный телевизор"