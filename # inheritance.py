# inheritance
'''
Наследование — это мощный механизм в объектно-ориентированном программировании, 
который позволяет одному классу наследовать атрибуты и методы другого класса. 
В Python, наследование позволяет создавать подклассы, 
которые расширяют или изменяют поведение родительских классов. 
Это способствует повторному использованию кода и улучшает организацию и модульность программы.

Давайте рассмотрим пример, 
в котором мы определим базовый класс и затем создадим подкласс, 
наследующий от него.
'''
### Пример: Базовый Класс и Подкласс

#### Базовый Класс


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"Транспортное средство: {self.make} {self.model}"

'''
Этот базовый класс `Vehicle` имеет атрибуты `make` и `model`, 
а также метод `display_info`, 
который выводит информацию о транспортном средстве.
'''
#### Подкласс


class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def display_info(self):
        original_info = super().display_info()
        return f"{original_info}, Год выпуска: {self.year}"

'''
Здесь `Car` является подклассом `Vehicle`. 
Он наследует атрибуты и методы `Vehicle`, 
но также вводит дополнительный атрибут `year`. 
В подклассе `Car` мы также переопределяем метод `display_info` 
для добавления информации о годе выпуска, 
при этом используя оригинальный метод `display_info` из 
`Vehicle` с помощью `super()`.
'''
#### Использование Классов


vehicle = Vehicle("Toyota", "Corolla")
print(vehicle.display_info())

car = Car("Ford", "Mustang", 2021)
print(car.display_info())

'''

В этом примере `Car` наследует функциональность от `Vehicle` 
и расширяет её. 
Метод `super().__init__(make, model)` 
вызывает конструктор родительского класса `Vehicle`, 
а `super().display_info()` 
вызывает оригинальный метод `display_info` родительского класса.

Таким образом, 
наследование позволяет классу `Car` 
переиспользовать код из класса `Vehicle`, 
добавляя к нему новые возможности и 
модифицируя существующие. 
Это обеспечивает чистоту и понятность кода, 
а также избегает его дублирования.

'''




'''

Давайте рассмотрим еще один пример наследования, 
на этот раз создадим базовый класс `Animal` и несколько подклассов, 
таких как `Dog` и `Cat`. 
В этом примере каждый подкласс будет наследовать свойства и 
методы базового класса `Animal`, 
но также будет иметь свои уникальные характеристики.

'''
### Пример: Класс `Animal` и Его Подклассы

#### Базовый Класс `Animal`


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        raise NotImplementedError("Subclass must implement this method")

    def __str__(self):
        return f"{self.name} is a {self.species}"

'''
В классе `Animal` определены два атрибута: 
`name` и `species`, 
а также метод `make_sound`, 
который предполагается переопределять в подклассах.
'''
#### Подкласс `Dog`


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof!"

'''
`Dog` наследуется от `Animal` и расширяет его, 
добавляя новый атрибут `breed` и переопределяя метод `make_sound`.
'''
#### Подкласс `Cat`


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color

    def make_sound(self):
        return "Meow!"

'''
Аналогично, `Cat` наследуется от `Animal`, 
добавляет атрибут `color` 
и переопределяет метод `make_sound`.
'''
#### Использование Классов


dog = Dog("Buddy", "Golden Retriever")
print(dog)  # Buddy is a Dog
print(dog.make_sound())  # Woof!

cat = Cat("Whiskers", "Black")
print(cat)  # Whiskers is a Cat
print(cat.make_sound())  # Meow!

'''

В этом примере подклассы `Dog` и `Cat` 
используют все свойства и методы базового класса `Animal`, 
но также вносят свои уникальные атрибуты и поведение. 
Это показывает, как наследование позволяет расширять и изменять функциональность базового класса, 
сохраняя при этом общую структуру и поведение.

'''

