# TODO: описать базовый класс

# TODO: описать дочерний класс

class Animal:
    """
    Базовый класс для всех животных.
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Инициализация животного.

        :param name: Имя животного.
        :param age: Возраст животного.
        """
        self._name = name  # Непубличный атрибут, чтобы защитить его от прямого изменения
        self._age = age    # Непубличный атрибут

    def speak(self) -> str:
        """
        Метод, возвращающий звук, который издает животное.
        По умолчанию возвращает 'Some sound'.
        """
        return "Some sound"

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Animal.
        """
        return f"{self.__class__.__name__}(Name: {self._name}, Age: {self._age})"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта Animal.
        """
        return f"Animal(name={self._name!r}, age={self._age!r})"


class Dog(Animal):
    """
    Класс для собак, наследующий от Animal.
    """

    def __init__(self, name: str, age: int, breed: str) -> None:
        """
        Инициализация собаки.

        :param name: Имя собаки.
        :param age: Возраст собаки.
        :param breed: Порода собаки.
        """
        super().__init__(name, age)  # Вызов конструктора базового класса
        self.breed = breed  # Публичный атрибут для породы

    def speak(self) -> str:
        """
        Метод, возвращающий звук, который издает собака.

        Переопределяет метод speak базового класса для возвращения
        специфичного звука для собак.
        """
        return "Woof!"

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Dog,
        включая информацию о породе.
        """
        return f"{super().__str__()}, Breed: {self.breed}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта Dog,
        включая информацию о породе.
        """
        return f"Dog(name={self._name!r}, age={self._age!r}, breed={self.breed!r})"


class Cat(Animal):
    """
    Класс для кошек, наследующий от Animal.
    """

    def __init__(self, name: str, age: int, color: str) -> None:
        """
        Инициализация кошки.

        :param name: Имя кошки.
        :param age: Возраст кошки.
        :param color: Цвет кошки.
        """
        super().__init__(name, age)  # Вызов конструктора базового класса
        self.color = color  # Публичный атрибут для цвета

    def speak(self) -> str:
        """
        Метод, возвращающий звук, который издает кошка.

        Переопределяет метод speak базового класса для возвращения
        специфичного звука для кошек.
        """
        return "Meow!"

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Cat,
        включая информацию о цвете.
        """
        return f"{super().__str__()}, Color: {self.color}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта Cat,
        включая информацию о цвете.
        """
        return f"Cat(name={self._name!r}, age={self._age!r}, color={self.color!r})"

if __name__ == "__main__":
    dog = Dog(name="Buddy", age=3, breed="Golden Retriever")
    cat = Cat(name="Whiskers", age=2, color="Black")

    print(dog)  # Выводит строковое представление собаки
    print(cat)  # Выводит строковое представление кошки

    print(dog.speak())  # Выводит "Woof!"
    print(cat.speak())  # Выводит "Meow!"