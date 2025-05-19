from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Абстрактный класс для продуктов"""

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other: Any) -> float:
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):  # type: ignore
        pass
