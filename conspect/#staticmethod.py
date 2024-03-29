#staticmethod


'''
Конечно, давайте подробно рассмотрим статические методы в Python, 
используя блок кода с пошаговыми комментариями и объяснениями. 
Статические методы - это методы, 
связанные с классом, а не с конкретным экземпляром класса. 
Они используются для выполнения задач, 
которые не требуют доступа к атрибутам экземпляра класса.

Для демонстрации статических методов, 
создадим класс `MathOperations`, 
в котором будет несколько статических методов для различных математических операций.

'''


class MathOperations:
    """
    Класс MathOperations содержит статические методы для выполнения базовых математических операций.

    Статические методы:
        add(x, y): Возвращает сумму двух чисел.
        subtract(x, y): Возвращает разность двух чисел.
        multiply(x, y): Возвращает произведение двух чисел.
        divide(x, y): Возвращает частное двух чисел.
    """

    @staticmethod
    def add(x, y):
        """
        Возвращает сумму двух чисел.

        Параметры:
            x (float): Первое число для сложения.
            y (float): Второе число для сложения.

        Возвращает:
            float: Результат сложения x и y.
        """
        return x + y

    @staticmethod
    def subtract(x, y):
        """
        Возвращает разность двух чисел.

        Параметры:
            x (float): Число, из которого вычитается.
            y (float): Число, которое вычитается.

        Возвращает:
            float: Результат вычитания y из x.
        """
        return x - y

    @staticmethod
    def multiply(x, y):
        """
        Возвращает произведение двух чисел.

        Параметры:
            x (float): Первый множитель.
            y (float): Второй множитель.

        Возвращает:
            float: Произведение x на y.
        """
        return x * y

    @staticmethod
    def divide(x, y):
        """
        Возвращает частное двух чисел.

        Параметры:
            x (float): Делимое.
            y (float): Делитель.

        Возвращает:
            float: Частное x и y. Если y равно 0, возвращает None.

        Исключения:
            ValueError: Если y равно 0.
        """
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y

# Пример использования статических методов
print("Сумма: ", MathOperations.add(10, 5))
print("Разность: ", MathOperations.subtract(10, 5))
print("Произведение: ", MathOperations.multiply(10, 5))
print("Деление: ", MathOperations.divide(10, 5))

'''
### Описание

1. **Определение класса `MathOperations`**: 
Этот класс содержит статические методы для выполнения арифметических операций.

2. **Статические методы**: 
Методы `add`, `subtract`, `multiply`, и `divide` определены как статические, 
что означает, 
что они могут быть вызваны непосредственно на уровне класса. 
Для этого используется декоратор `@staticmethod`.

3. **Работа методов**: 
Каждый метод принимает два параметра (`x` и `y`) 
и возвращает результат соответствующей математической операции. 
В методе `divide` добавлена проверка на деление на ноль.

4. **Вызов статических методов**: 
Для использования статических методов не нужно создавать экземпляр класса. 
Методы вызываются непосредственно через имя класса, как показано в примерах использования.
'''

'''
Статические методы в Python могут быть вызваны как через класс, 
так и через экземпляр класса. 
Важно отметить, что статические методы не имеют доступа к атрибутам экземпляра (`self`) 
или класса (`cls`), 
поскольку они не получают ссылку на экземпляр или класс в качестве первого аргумента. 
Они ведут себя похоже на обычные функции, 
но принадлежат пространству имен класса.

Давайте рассмотрим на примере с классом 
`Car` и статическим методом `is_vintage`.
'''
### Пример Статического Метода


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @staticmethod
    def is_vintage(year):
        current_year = 2024
        return current_year - year >= 25

# Создание экземпляра класса
my_car = Car("Ford", "Mustang", 1967)

# Вызов статического метода через класс
print("Винтажный (через класс):", Car.is_vintage(1967))

# Вызов статического метода через экземпляр
print("Винтажный (через экземпляр):", my_car.is_vintage(1967))

'''

В этом примере `is_vintage` 
является статическим методом класса `Car`. 

1. **Вызов через класс**: 
`Car.is_vintage(1967)` вызывает метод `is_vintage` 
непосредственно через класс `Car`.

2. **Вызов через экземпляр**: 
`my_car.is_vintage(1967)` вызывает тот же метод `is_vintage`, 
но через экземпляр `my_car` класса `Car`. 
Несмотря на то, что метод вызывается через экземпляр, 
он всё равно не имеет доступа к атрибутам этого конкретного экземпляра.

Таким образом, 
статический метод может быть вызван как через сам класс, 
так и через экземпляр класса, 
но его поведение остается неизменным, 
не зависимо от способа вызова.


'''


'''

Конечно, давайте рассмотрим еще один пример, 
чтобы лучше понять использование статических методов в Python. 
На этот раз создадим класс `TemperatureConverter` 
с статическими методами для конвертации температуры между шкалами Цельсия и Фаренгейта.

'''
### Пример: Класс `TemperatureConverter` с Статическими Методами


class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """
        Конвертирует температуру из Цельсия в Фаренгейты.

        Параметры:
            celsius (float): Температура в градусах Цельсия.

        Возвращает:
            float: Температура в градусах Фаренгейта.
        """
        return celsius * 9.0 / 5.0 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        """
        Конвертирует температуру из Фаренгейтов в Цельсии.

        Параметры:
            fahrenheit (float): Температура в градусах Фаренгейта.

        Возвращает:
            float: Температура в градусах Цельсия.
        """
        return (fahrenheit - 32) * 5.0 / 9.0

# Вызов статических методов через класс
celsius = TemperatureConverter.fahrenheit_to_celsius(100)
print("100 Фаренгейтов в Цельсиях:", celsius)

fahrenheit = TemperatureConverter.celsius_to_fahrenheit(0)
print("0 Цельсия в Фаренгейтах:", fahrenheit)

# Создание экземпляра класса не требуется, но его можно использовать для вызова статических методов
converter = TemperatureConverter()
celsius = converter.fahrenheit_to_celsius(68)
print("68 Фаренгейтов в Цельсиях:", celsius)

fahrenheit = converter.celsius_to_fahrenheit(20)
print("20 Цельсия в Фаренгейтах:", fahrenheit)


'''

В этом примере:

1. **Статические методы для конвертации температур**: 
`celsius_to_fahrenheit` и 
`fahrenheit_to_celsius` являются статическими методами, 
которые выполняют конвертацию температур между двумя шкалами.

2. **Вызов через класс**: 
Методы вызываются напрямую через класс 
`TemperatureConverter`, 
что является обычным использованием статических методов.

3. **Вызов через экземпляр**: 
Хотя создание экземпляра 
`TemperatureConverter` не обязательно для использования статических методов, 
мы всё равно можем создать экземпляр и 
использовать его для вызова этих методов. 
Поведение методов останется таким же, 
как при вызове через класс.

Этот пример иллюстрирует, 
как статические методы могут быть полезны для выполнения задач, 
которые логически связаны с классом, 
но не зависят от состояния конкретного экземпляра этого класса.
'''

'''
Атрибуты класса в Python — это переменные, 
которые принадлежат самому классу, 
а не конкретным экземплярам этого класса. 
Эти атрибуты общие для всех экземпляров класса. 
По сути, они являются глобальными переменными внутри класса. 
Атрибуты класса определяются внутри тела класса, 
но вне любых методов класса.

рассмотрим пример с использованием атрибутов класса.
'''
### Пример: Класс с Атрибутами Класса


class Vehicle:
    # Атрибут класса, общий для всех экземпляров
    total_vehicles = 0

    def __init__(self, make, model):
        self.make = make  # Атрибут экземпляра
        self.model = model  # Атрибут экземпляра
        Vehicle.total_vehicles += 1  # Увеличение атрибута класса

    @classmethod
    def number_of_vehicles(cls):
        """
        Возвращает общее количество транспортных средств, созданных в классе.

        Возвращает:
            int: Общее количество транспортных средств.
        """
        return cls.total_vehicles

# Создание экземпляров Vehicle
v1 = Vehicle("Toyota", "Corolla")
v2 = Vehicle("Honda", "Accord")

# Доступ к атрибуту класса
print("Общее количество транспортных средств:", Vehicle.total_vehicles)

# Использование метода класса для доступа к атрибуту класса
print("Число транспортных средств через метод класса:", Vehicle.number_of_vehicles())



'''
В этом примере:

1. **Атрибут класса `total_vehicles`**: 
    Определен в классе `Vehicle` и является общим для всех экземпляров. 
    Каждый раз при создании нового экземпляра `Vehicle` 
    значение `total_vehicles` увеличивается на единицу.

2. **Атрибуты экземпляра**: 
    `make` и `model` являются атрибутами экземпляра, 
    уникальными для каждого созданного объекта `Vehicle`.

3. **Метод класса `number_of_vehicles`**: 
    Это метод класса, использующий декоратор `@classmethod`. 
    Он позволяет нам работать с атрибутом класса `total_vehicles`.

Атрибуты класса полезны для хранения значений, 
которые должны быть общими для всех экземпляров класса. 
Они часто используются для определения констант или для отслеживания общего состояния для всех экземпляров класса.
'''




'''
Конечно, давайте рассмотрим еще один пример, чтобы углубить понимание атрибутов класса. На этот раз создадим класс `Book`, который будет иметь атрибуты класса для отслеживания общего количества книг и списка всех книг. Каждый экземпляр класса `Book` будет иметь свои уникальные атрибуты, такие как название и автор.

### Пример: Класс `Book` с Атрибутами Класса

'''
class Book:
    total_books = 0  # Атрибут класса для подсчета общего числа книг
    book_list = []   # Атрибут класса для хранения списка всех книг

    def __init__(self, title, author):
        self.title = title  # Атрибут экземпляра
        self.author = author  # Атрибут экземпляра
        Book.total_books += 1  # Увеличиваем счетчик общего числа книг
        Book.book_list.append(f"{title} by {author}")  # Добавляем книгу в список

    @classmethod
    def get_book_info(cls):
        """
        Возвращает информацию о всех книгах и их общем числе.

        Возвращает:
            str: Информация о всех книгах и их общем числе.
        """
        info = f"Total Books: {cls.total_books}\n"
        info += "Book List:\n" + "\n".join(cls.book_list)
        return info

# Создание экземпляров Book
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

# Вывод информации обо всех книгах
print(Book.get_book_info())

'''

В этом примере:

1. **Атрибуты класса 
`total_books` и 
`book_list`**: 
Определены в классе `Book` и общие для всех экземпляров. 
`total_books` используется для подсчета количества созданных книг, 
а `book_list` хранит информацию о всех книгах.

2. **Атрибуты экземпляра 
`title` и 
`author`**: 
Уникальны для каждого экземпляра класса `Book` 
и хранят информацию о названии и авторе книги.

3. **Метод класса 
`get_book_info`**: 
Этот метод возвращает общую информацию о всех книгах 
и их общее количество, 
используя атрибуты класса.

Этот пример демонстрирует, 
как атрибуты класса могут быть использованы для отслеживания общей информации, 
связанной со всеми экземплярами класса. 
Атрибуты экземпляра используются для хранения информации, 
специфичной для каждого отдельного объекта.

'''


'''

Магические методы в Python, 
также известные как специальные методы, 
начинаются и заканчиваются двойными подчеркиваниями 
(например, `__init__`, `__str__`, `__len__`). 
Они позволяют вашим классам имитировать поведение встроенных типов данных 
и взаимодействовать с ключевыми языковыми конструкциями 
(например, циклами, операторами, функциями `len()` и `str()`).

Давайте рассмотрим несколько распространенных магических методов на примере:
'''
### Пример: Класс `Book` с Магическими Методами


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """
        Возвращает строковое представление объекта.
        """
        return f"'{self.title}' by {self.author}"

    def __len__(self):
        """
        Возвращает количество страниц в книге.
        """
        return self.pages

    def __del__(self):
        """
        Вызывается, когда экземпляр удаляется.
        """
        print(f"The book '{self.title}' has been deleted.")

# Создание и использование экземпляра Book
book = Book("1984", "George Orwell", 328)
print(book)  # Вызывает метод __str__
print(len(book))  # Вызывает метод __len__

# Удаление экземпляра book
del book  # Вызывает метод __del__

'''

В этом примере:

1. **`__init__`**: 
Конструктор класса, который инициализирует новый экземпляр.

2. **`__str__`**: 
Определяет, как экземпляр класса будет представлен в виде строки, 
например, при печати.

3. **`__len__`**: 
Позволяет использовать функцию `len()` с экземпляром класса. 
В данном случае возвращает количество страниц в книге.

4. **`__del__`**: 
Этот метод вызывается при уничтожении экземпляра класса 
(например, при его удалении с помощью `del`). 
Может быть использован для выполнения "завершающих" операций, 
таких как закрытие файлов или освобождение ресурсов.

Магические методы — 
мощный инструмент в объектно-ориентированном программировании Python, 
позволяющий классам имитировать поведение встроенных типов и взаимодействовать 
с различными частями языка Python.

'''



'''

Давайте рассмотрим другой пример, 
в котором мы создадим класс `ComplexNumber` 
для представления комплексных чисел и 
реализуем несколько магических методов для 
выполнения арифметических операций, 
сравнения и других действий.

'''
### Пример: Класс `ComplexNumber` с Магическими Методами

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __abs__(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    def __repr__(self):
        return f"ComplexNumber({self.real}, {self.imag})"

# Создание и использование экземпляров ComplexNumber
c1 = ComplexNumber(3, 2)
c2 = ComplexNumber(1, 7)

print("Сложение:", c1 + c2)  # Вызывает __add__
print("Вычитание:", c1 - c2)  # Вызывает __sub__
print("Умножение:", c1 * c2)  # Вызывает __mul__
print("Равенство:", c1 == c2)  # Вызывает __eq__
print("Модуль:", abs(c1))     # Вызывает __abs__
print("Представление:", repr(c1))  # Вызывает __repr__

'''

В этом примере:

1. **`__init__`**: 
Конструктор класса для инициализации реальной и мнимой частей.

2. **`__str__` и `__repr__`**: `__str__` 
определяет удобочитаемое строковое представление объекта, 
в то время как `__repr__` 
предназначен для однозначного представления объекта.

3. **Арифметические операции**: 
Методы `__add__`, `__sub__`, и `__mul__` определяют, 
как выполнять сложение, 
вычитание и умножение между двумя комплексными числами соответственно.

4. **`__eq__`**: 
Метод для сравнения двух комплексных чисел на равенство.

5. **`__abs__`**: 
Определяет, как вычислять абсолютное значение (модуль) комплексного числа.

Этот пример показывает, 
как магические методы позволяют объектам класса `ComplexNumber` 
вести себя как встроенные числовые типы данных в Python, 
поддерживая арифметические операции, сравнения и другие стандартные функции.

'''


