BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]
class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


if __name__ == 'main':
    # Инициализируем список книг, используя данные из BOOKS_DATABASE
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"])
        for book_dict in BOOKS_DATABASE
    ]

    # Выводим информацию о каждой книге, используя метод str
    for book in list_books:
        print(book)  # Это автоматически вызовет метод str()

    # Выводим представление списка, используя метод repr
    print(list_books)  # Это автоматически вызовет метод repr для каждого элемента
