#
# Домашня робота 3:
#
#  - доробити ДЗ другого дня з урахуванням додатково отриманих знань про GIT: гілки і колективна робота
#  - ДЗ третього дня:
#  - Уявіть що ми з Вами пишемо застосунок що допоможе офлайн-бібліотеці мати онлайн-представництво.
#  І нам необхідно описати сутності, якими оперує онлайн бібліотека - книжки.
#  - Кожна книжка має атрибути
#  - Назву
#  - Опис
#  - Мова книги
#  - Список авторів (!!)
#  - Список літературних жанрів до яких вона віднесена (!!)
#  - Рік видання
#  - ISBN (хто не знає що це таке - загугліть)
#
# Вам треба описати:
#  - клас книги
#  - Клас автора (поля: first_name, last_name, year_of_birth)
#  - Клас жанру книги (поля назва жанру, опис жанру)
#
#
# Клас книги використовує класи автор і жанр для визначення своїх полів.
#
#
# Реалізуйте методи __str__ і __repr__ для всіх класів.
# Реалізуйте метод __eq__ для авторів (авторів вважаємо однаковими якщо всі атрибути однакові) і
# для книги (книги вважаються однаковими якщо однакові назви і мають тих самих авторів).
#
#
# Всі методи повинні бути документовані і анотовані.
#
# Код повинен бути реалізований в окремій гілці, запущений в репозиторій створений MR.
# Бажано запросити когось з колег в репозиторій і попросити зробити code review (не обовʼязково).
#
# Після апруву MR вмерджіть код в головну гілку.
from typing import Optional


class Genre:
    def __init__(self, name: str, description: Optional[str] = None) -> None:
        self.name = name
        self.description = description

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Genre({self.name}, {self.description})"


class Author:
    def __init__(
        self, first_name: str, last_name: str, year_of_birth: Optional[int] = None
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __repr__(self) -> str:
        return f"Author({self.first_name}, {self.last_name}, {self.year_of_birth})"

    def __eq__(self, other: "Author") -> bool:
        if not isinstance(other, Author):
            raise TypeError(
                f"for type Author and type {type(other)} operation is not implemented"
            )
        return (
            self.first_name == other.first_name
            and self.last_name == other.last_name
            and self.year_of_birth == other.year_of_birth
        )

    def __hash__(self):
        return hash((self.first_name, self.last_name, self.year_of_birth))


class Book:
    def __init__(
        self,
        name: str,
        language: str,
        authors: list[Author],
        genres: list[Genre],
        year: int,
        isbn: str,
        describe: Optional[str] = None,
    ):
        self.name = name
        self.language = language
        self.authors = authors
        self.genres = genres
        self.year = year
        self.isbn = isbn
        self.describe = describe

    def __eq__(self, other: "Book") -> bool:
        return set(self.authors) == set(other.authors) and self.name == other.name
