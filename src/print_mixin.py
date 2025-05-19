class PrintMixin:
    """Класс миксин для вывода в консоль информации об объекте"""

    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
