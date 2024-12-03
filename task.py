import doctest


class Stack:
    def __init__(self, max_size: int, name: str):
        if max_size <= 0:
            raise ValueError("Max size must be a positive integer.")
        self.items = []
        self.max_size = max_size
        self.name = name

    def push(self, item: int) -> None:
        """
        Push an item onto the stack.
        Args:
            item (int): The item to push onto the stack.
        Raises:
            OverflowError: If the stack is full.
        Example:
            >>> stack = Stack(2, "TestStack")
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.items
            [1, 2]
        """
        if len(self.items) >= self.max_size:
            raise OverflowError("Push to a full stack.")
        self.items.append(item)

    def pop(self) -> int:
        """
        Pop an item off the stack.
        Returns:
            int: The item popped off the stack.
        Raises:
            IndexError: If the stack is empty.
        Example:
            >>> stack = Stack(2, "TestStack")
            >>> stack.push(1)
            >>> stack.pop()
            1
        """
        if not self.items:
            raise IndexError("Pop from an empty stack.")
        return self.items.pop()

    def peek(self) -> int:
        """
        Peek at the top item of the stack without removing it.
        Returns:
            int: The top item of the stack.
        Raises:
            IndexError: If the stack is empty.
        Example:
            >>> stack = Stack(2, "TestStack")
            >>> stack.push(1)
            >>> stack.peek()
            1
        """
        if not self.items:
            raise IndexError("Peek from an empty stack.")
        return self.items[-1]

    def is_empty(self) -> bool:
        """
        Check if the stack is empty.
        Returns:
            bool: True if the stack is empty, False otherwise.
        Example:
            >>> stack = Stack(2, "TestStack")
            >>> stack.is_empty()
            True
        """
        return len(self.items) == 0

    def is_full(self) -> bool:
        """
        Check if the stack is full.
        Returns:
            bool: True if the stack is full, False otherwise.
        Example:
            >>> stack = Stack(2, "TestStack")
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.is_full()
            True
        """
        return len(self.items) == self.max_size


class Book:
    """Класс, представляющий книгу.
    Атрибуты:
    title (str): Название книги.
    year (int): Год выпуска книги.
    Методы:    get_info: Возвращает информацию о книге.
    check_availability: Проверяет, не является ли книга устаревшей (выпущена более 50 лет назад)."""

    def __init__(self, title: str, year: int):
        """
        Инициализирует объект книги с названием и годом выпуска.
        Аргументы:
        title (str): Название книги.
        year (int): Год выпуска книги.
        Исключения:
        ValueError: Если год выпуска меньше 1450 (первое массовое книгопечатание).
        """
        self.title = title
        self.year = year

    def get_info(self) -> str:
        """
        Возвращает строку с информацией о книге.
        Возвращаемое значение:
        str: Строка с названием и годом выпуска книги.
        Пример:
        >>> book = Book("1984", 1949)
        >>> book.get_info()
        'Книга: 1984, Год выпуска: 1949'
        """
        return f"Книга: {self.title}, Год выпуска: {self.year}"

    def check_availability(self, current_year: int = 2024) -> bool:
        """
        Проверяет, является ли книга устаревшей (выпущена более 50 лет назад).
        Аргументы:
current_year (int, по умолчанию 2024): Текущий год.
        Возвращаемое значение:
        bool: True, если книга устаревшая, False — если нет.
        Пример:
        >>> book = Book("1984", 1949)
        >>> book.check_availability()
        True
        """
        if current_year < 0:
            raise ValueError("Неправильный год")
        return current_year - self.year > 50


class Car:
    """Класс, представляющий автомобиль.
    Атрибуты:
    brand (str): Марка автомобиля.
    max_speed (int): Максимальная скорость автомобиля в км/ч.
    Методы: get_info: Возвращает информацию о марке и максимальной скорости автомобиля.
    is_speed_legal: Проверяет, не превышает ли скорость автомобиля установленное ограничение."""

    def __init__(self, brand: str, max_speed: int):
        """
        Инициализирует объект автомобиля с маркой и максимальной скоростью.
        Аргументы:
        brand (str): Марка автомобиля.
        max_speed (int): Максимальная скорость автомобиля.
        Исключения:
        ValueError: Если максимальная скорость меньше 50 или больше 300.
        """
        if not (50 <= max_speed <= 300):
            raise ValueError("Максимальная скорость должна быть между 50 и 300 км/ч.")
        self.brand = brand
        self.max_speed = max_speed

    def get_info(self) -> str:
        """
        Возвращает строку с информацией о марке и максимальной скорости автомобиля.
        Возвращаемое значение:
        str: Строка с маркой и максимальной скоростью.
        Пример:
        >>> car = Car("BMW", 250)
        >>> car.get_info()
        'Марка: BMW, Максимальная скорость: 250 км/ч'
        """
        return f"Марка: {self.brand}, Максимальная скорость: {self.max_speed} км/ч"

    def is_speed_legal(self, speed_limit: int) -> bool:
        """
        Проверяет, не превышает ли максимальная скорость автомобиля установленное ограничение.
        Аргументы:
        speed_limit (int): Лимит скорости.
        Возвращаемое значение:
        bool: True, если скорость не превышает ограничение, False — если превышает.
        Пример:
        >>> car = Car("BMW", 250)
        >>> car.is_speed_legal(200)
        False
        """
        if speed_limit < 0:
            raise ValueError("Скорость не может быть отрицательной")
        return self.max_speed <= speed_limit


if __name__ == "main":
    doctest.testmod()  # тестирование примеров, которые находятся в документации