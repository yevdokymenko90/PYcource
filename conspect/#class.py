#class

'''
Конечно, давайте начнем с основ классов в Python. 
Я создам пример класса, 
который представляет собой простой калькулятор. 
Этот класс будет иметь методы для основных арифметических операций. 
Я подробно прокомментирую код, 
чтобы вы могли понять каждый его аспект.
'''

class SimpleCalculator:
    """
    Класс SimpleCalculator предназначен для выполнения базовых арифметических операций.

    Методы:
        add(x, y): Возвращает сумму x и y.
        subtract(x, y): Возвращает разность x и y.
        multiply(x, y): Возвращает произведение x и y.
        divide(x, y): Возвращает частное x и y.
    """

    def add(self, x, y):
        """
        Возвращает сумму двух чисел.

        Параметры:
            x (float): Первое число для сложения.
            y (float): Второе число для сложения.

        Возвращает:
            float: Результат сложения x и y.
        """
        return x + y

    def subtract(self, x, y):
        """
        Возвращает разность двух чисел.

        Параметры:
            x (float): Число, из которого вычитается.
            y (float): Число, которое вычитается.

        Возвращает:
            float: Результат вычитания y из x.
        """
        return x - y

    def multiply(self, x, y):
        """
        Возвращает произведение двух чисел.

        Параметры:
            x (float): Первый множитель.
            y (float): Второй множитель.

        Возвращает:
            float: Произведение x на y.
        """
        return x * y

    def divide(self, x, y):
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

# Пример использования класса
calc = SimpleCalculator()
print("Сумма: ", calc.add(10, 5))
print("Разность: ", calc.subtract(10, 5))
print("Произведение: ", calc.multiply(10, 5))
print("Деление: ", calc.divide(10, 5))


'''

В этом примере:

1. **Определение класса**: `class SimpleCalculator:` создает новый класс с именем `SimpleCalculator`.

2. **Методы класса**: 
`add`, 
`subtract`, 
`multiply`, и 
`divide` являются методами класса. 
Каждый метод принимает `self` (который представляет экземпляр класса) 
и два числа `x` и `y`.

3. **Документация**: 
Строки, заключенные в тройные кавычки (`"""`), 
являются строками документации (docstrings), 
которые описывают назначение класса и его методов.

4. **Исключение**: 
В методе `divide` используется проверка, 
чтобы избежать деления на ноль. 
В случае, если `y` равно нулю, 
выбрасывается исключение `ValueError`.

5. **Создание объекта и использование методов**: 
В конце мы создаем объект `calc` класса `SimpleCalculator` 
и вызываем его методы для выполнения арифметических операций. 

Этот пример является хорошим стартовым пунктом 
для понимания основ работы с классами в Python.
'''



'''
Отлично! Теперь давайте расширим наш пример, 
добавив в класс `SimpleCalculator` 
дополнительные функции и концепции. 
Мы добавим метод для возведения числа в степень 
и метод для вычисления квадратного корня. 
Также включим конструктор класса (`__init__`) 
и переменную экземпляра для хранения истории операций.
'''

import math

class SimpleCalculator:
    """
    Класс SimpleCalculator предназначен для выполнения арифметических операций.

    Атрибуты:
        history (list of str): Хранит историю выполненных операций.

    Методы:
        add(x, y), subtract(x, y), multiply(x, y), divide(x, y): Арифметические операции.
        power(x, y): Возвращает x в степени y.
        sqrt(x): Возвращает квадратный корень из x.
        print_history(): Печатает историю операций.
    """

    def __init__(self):
        """
        Инициализатор класса. Создает экземпляр класса SimpleCalculator.

        Атрибуты:
            history (list of str): Инициализируется пустым списком.
        """
        self.history = []

    # Методы add, subtract, multiply, divide опущены для краткости

    def power(self, x, y):
        """
        Возвращает x в степени y.

        Параметры:
            x (float): Основание степени.
            y (float): Показатель степени.

        Возвращает:
            float: Результат возведения x в степень y.
        """
        result = x ** y
        self.history.append(f"{x} ^ {y} = {result}")
        return result

    def sqrt(self, x):
        """
        Возвращает квадратный корень из x.

        Параметры:
            x (float): Число, из которого извлекается квадратный корень.

        Возвращает:
            float: Квадратный корень из x.

        Исключения:
            ValueError: Если x отрицательный.
        """
        if x < 0:
            raise ValueError("Cannot take the square root of a negative number.")
        result = math.sqrt(x)
        self.history.append(f"sqrt({x}) = {result}")
        return result

    def print_history(self):
        """
        Печатает историю выполненных операций.
        """
        print("История операций:")
        for operation in self.history:
            print(operation)

# Пример использования класса
calc = SimpleCalculator()
print("Степень: ", calc.power(2, 3))
print("Квадратный корень: ", calc.sqrt(16))
calc.print_history()

'''
В этом расширенном примере:

1. **Импорт модуля**: 
Мы импортировали модуль `math` 
для использования функции `sqrt` 
при вычислении квадратного корня.

2. **Инициализатор `__init__`**: 
Этот специальный метод вызывается при 
создании нового объекта класса. 
Здесь он используется для инициализации списка `history`, 
который будет хранить историю операций.

3. **Новые методы**: 
Методы `power` и `sqrt` 
добавлены для расширения функциональности калькулятора.

4. **Обработка исключений**: 
В методе `sqrt` добавлена проверка, 
чтобы избежать извлечения квадратного корня из отрицательного числа.

5. **Сохранение истории**: 
Каждый метод, выполняющий операцию, добавляет запись в историю.

6. **Метод `print_history`**: 
Этот метод позволяет распечатать всю историю выполненных операций.

Этот пример помогает понять, 
как расширять классы новыми функциями 
и как управлять состоянием объекта в Python.

'''



'''
Отлично! 
Теперь давайте добавим к нашему классу `SimpleCalculator` 
ещё больше возможностей. 
Мы включим функционал для работы с 
памятью калькулятора, 
позволяя сохранять и восстанавливать результаты. 
Это демонстрирует использование 
приватных переменных и методов, 
а также пример работы 
с property-декораторами в Python.

'''
class SimpleCalculator:
    """
    Класс SimpleCalculator предназначен для выполнения арифметических операций и работы с памятью.

    Атрибуты:
        _memory (float): Приватный атрибут для хранения значения в памяти.

    Методы:
        add(x, y), subtract(x, y), multiply(x, y), divide(x, y), power(x, y), sqrt(x): Арифметические операции.
        print_history(): Печатает историю операций.
        save_to_memory(value): Сохраняет значение в память.
        clear_memory(): Очищает память.
        memory: Свойство для доступа к значению в памяти.
    """

    def __init__(self):
        self.history = []
        self._memory = None  # Инициализация приватной переменной памяти

    # Методы add, subtract, multiply, divide, power, sqrt и print_history опущены для краткости

    def save_to_memory(self, value):
        """
        Сохраняет значение в память калькулятора.

        Параметры:
            value (float): Значение для сохранения в память.
        """
        self._memory = value

    def clear_memory(self):
        """
        Очищает память калькулятора.
        """
        self._memory = None

    @property
    def memory(self):
        """
        Возвращает значение, сохраненное в памяти.

        Возвращает:
            float: Значение в памяти.
        """
        return self._memory

    @memory.setter
    def memory(self, value):
        """
        Устанавливает значение в память калькулятора.

        Параметры:
            value (float): Значение для установки в память.
        """
        self._memory = value

# Пример использования класса с функциями памяти
calc = SimpleCalculator()
calc.save_to_memory(50)
print("Значение в памяти: ", calc.memory)
calc.memory = 100
print("Обновленное значение в памяти: ", calc.memory)
calc.clear_memory()
print("Память после очистки: ", calc.memory)

'''
В этом обновлении класса `SimpleCalculator`:

1. **Приватная переменная `_memory`**: 
Используется для хранения значения в памяти калькулятора. 
Префикс с подчеркиванием (`_`) указывает на то, 
что это приватный атрибут класса.

2. **Методы для работы с памятью**: 
Методы `save_to_memory`, 
`clear_memory` и свойства `memory` (с геттером и сеттером) 
предоставляют интерфейс для управления значением в памяти.

3. **Property-декораторы**: 
Используются для создания геттера и сеттера для атрибута `memory`. 
Это позволяет контролировать доступ к приватной переменной `_memory`, 
обеспечивая инкапсуляцию данных.

Этот пример показывает, 
как можно управлять доступом к внутреннему состоянию объекта 
и обеспечивать инкапсуляцию через приватные атрибуты и свойства. 
Также демонстрируется использование property-декораторов для создания геттеров и сеттеров в Python.
'''

'''
Прекрасно, 
давайте продолжим расширять наш `SimpleCalculator`, 
вводя концепции наследования и полиморфизма. 

Мы создадим подкласс 
`AdvancedCalculator`, 
который расширяет функциональность 
`SimpleCalculator` дополнительными математическими операциями, 
такими как вычисление факториала и логарифмов. 

Это позволит нам углубить понимание наследования 
и переопределения методов в Python.

'''
import math

class AdvancedCalculator(SimpleCalculator):
    """
    Класс AdvancedCalculator расширяет SimpleCalculator, добавляя продвинутые математические функции.

    Методы:
        factorial(x): Возвращает факториал x.
        log(x, base): Возвращает логарифм x по основанию base.
    """

    def factorial(self, x):
        """
        Возвращает факториал числа x.

        Параметры:
            x (int): Число для вычисления факториала.

        Возвращает:
            int: Факториал числа x.

        Исключения:
            ValueError: Если x отрицательный или нецелочисленный.
        """
        if not isinstance(x, int) or x < 0:
            raise ValueError("Factorial is only defined for non-negative integers.")
        return math.factorial(x)

    def log(self, x, base):
        """
        Возвращает логарифм x по основанию base.

        Параметры:
            x (float): Число для вычисления логарифма.
            base (float): Основание логарифма.

        Возвращает:
            float: Логарифм x по основанию base.

        Исключения:
            ValueError: Если x или base отрицательные или равные нулю.
        """
        if x <= 0 or base <= 0:
            raise ValueError("Logarithm and base should be greater than 0.")
        return math.log(x, base)

# Пример использования класса AdvancedCalculator
adv_calc = AdvancedCalculator()
print("Факториал: ", adv_calc.factorial(5))
print("Логарифм: ", adv_calc.log(100, 10))
adv_calc.save_to_memory(adv_calc.factorial(5))
print("Значение в памяти: ", adv_calc.memory)

'''
В этом примере:

1. **Наследование**: 
`AdvancedCalculator` наследует все методы и атрибуты от 
`SimpleCalculator`. 

Это позволяет `AdvancedCalculator` 
использовать базовые арифметические операции, 
а также методы работы с памятью.

2. **Новые методы**: 
Мы добавили методы `factorial` и `log`, 
которые представляют более сложные математические операции.

3. **Исключения**: 
В методах `factorial` и `log` 
добавлена проверка входных параметров, 
и в случае недопустимых значений выбрасываются исключения.

4. **Использование методов базового класса**: 
В примере использования мы вызываем метод `save_to_memory` 
базового класса `SimpleCalculator` 
для сохранения результата операции в память.

Этот пример иллюстрирует, 
как можно использовать наследование 
для расширения функциональности существующих классов, 
а также принципы полиморфизма и инкапсуляции 
в объектно-ориентированном программировании Python.
'''



'''
Теперь давайте добавим в наш `AdvancedCalculator` 
ещё несколько функций, 
а также познакомимся с концепцией перегрузки методов 
и использования декораторов. 
Мы добавим методы для работы с комплексными числами 
и перегрузим некоторые существующие методы, 
чтобы они могли обрабатывать комплексные числа.

'''
class AdvancedCalculator(SimpleCalculator):
    """
    Класс AdvancedCalculator, расширяющий SimpleCalculator с дополнительными математическими функциями,
    включая поддержку комплексных чисел.

    Методы:
        factorial(x), log(x, base): Наследуются из SimpleCalculator.
        add_complex(a, b): Складывает два комплексных числа.
        subtract_complex(a, b): Вычитает два комплексных числа.
    """

    def add_complex(self, a, b):
        """
        Возвращает сумму двух комплексных чисел.

        Параметры:
            a (complex): Первое комплексное число.
            b (complex): Второе комплексное число.

        Возвращает:
            complex: Результат сложения a и b.
        """
        return a + b

    def subtract_complex(self, a, b):
        """
        Возвращает разность двух комплексных чисел.

        Параметры:
            a (complex): Комплексное число, из которого вычитается.
            b (complex): Комплексное число, которое вычитается.

        Возвращает:
            complex: Результат вычитания b из a.
        """
        return a - b

    def multiply(self, x, y):
        """
        Переопределяет метод multiply, позволяя умножать комплексные числа.

        Параметры:
            x (float или complex): Первый множитель.
            y (float или complex): Второй множитель.

        Возвращает:
            float или complex: Произведение x на y.
        """
        return x * y

    def divide(self, x, y):
        """
        Переопределяет метод divide, позволяя делить комплексные числа.

        Параметры:
            x (float или complex): Делимое.
            y (float или complex): Делитель.

        Возвращает:
            float или complex: Частное x и y.
        """
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y

# Пример использования класса с комплексными числами
adv_calc = AdvancedCalculator()
print("Сложение комплексных чисел: ", adv_calc.add_complex(1 + 2j, 3 + 4j))
print("Вычитание комплексных чисел: ", adv_calc.subtract_complex(1 + 2j, 3 + 4j))
print("Умножение комплексных чисел: ", adv_calc.multiply(1 + 2j, 3 + 4j))
print("Деление комплексных чисел: ", adv_calc.divide(1 + 2j, 3 + 4j))


'''
В этом расширении `AdvancedCalculator`:

1. **Новые методы для комплексных чисел**: 
Методы `add_complex` 
и `subtract_complex` добавлены для работы с комплексными числами.

2. **Перегрузка методов**: 
Методы `multiply` и `divide` 
были переопределены, 
чтобы поддерживать операции не только с обычными числами, 
но и с комплексными.

3. **Поддержка разных типов данных**: 
Методы теперь могут работать как с обычными (`float`), 
так и с комплексными числами (`complex`).

Этот пример показывает, 
как можно расширить класс, 
добавив поддержку новых типов данных и переопределив существующие методы, 
что является важной частью полиморфизма в объектно-ориентированном программировании.
'''


'''

Далее, давайте обогатим наш `AdvancedCalculator` 
возможностью обработки исключений и логирования. 
Это позволит нам не только обрабатывать ошибки более эффективно, 
но и отслеживать ход выполнения операций. 
Для этого мы добавим модуль логирования и 
переопределим некоторые методы для логирования операций и 
обработки исключений.

'''

import logging
import math

# Настройка базового конфига логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AdvancedCalculator(SimpleCalculator):
    """
    Класс AdvancedCalculator с расширенными функциями и логированием.

    Методы:
        factorial(x), log(x, base), add_complex(a, b), subtract_complex(a, b): Наследуются из предыдущего определения.
        multiply(x, y), divide(x, y): Переопределенные методы с логированием и обработкой исключений.
    """

    def multiply(self, x, y):
        try:
            result = x * y
            logging.info(f"Умножение: {x} * {y} = {result}")
            return result
        except Exception as e:
            logging.error(f"Ошибка при умножении: {e}")
            raise

    def divide(self, x, y):
        try:
            if y == 0:
                raise ValueError("Невозможно разделить на ноль.")
            result = x / y
            logging.info(f"Деление: {x} / {y} = {result}")
            return result
        except Exception as e:
            logging.error(f"Ошибка при делении: {e}")
            raise

# Пример использования класса с логированием
adv_calc = AdvancedCalculator()
try:
    print("Умножение комплексных чисел: ", adv_calc.multiply(1 + 2j, 3 + 4j))
    print("Деление комплексных чисел: ", adv_calc.divide(1 + 2j, 0))
except Exception as e:
    print(f"Поймано исключение: {e}")

'''
В этом обновлении `AdvancedCalculator`:

1. **Настройка логирования**: 
Используется модуль `logging` для настройки основного логгера. 
Мы настроили его на уровне `INFO`, 
чтобы записывать информационные сообщения и ошибки.

2. **Логирование операций**: 
В методах `multiply` и `divide` теперь добавлено логирование, 
которое записывает информацию о каждой операции.

3. **Обработка исключений**: 
В тех же методах добавлена обработка исключений с логированием ошибок. 
Это позволяет нам отслеживать исключения и логировать их, не прерывая работу программы.

4. **Проверка исключений**: 
В примере использования класса демонстрируется, как обрабатывать исключения, 
которые могут быть вызваны во время выполнения операций.

Этот пример иллюстрирует, 
как можно использовать логирование и 
обработку исключений для улучшения надежности и 
отслеживаемости кода в Python. 
Логирование — ключевой элемент при разработке более сложных приложений, 
а корректная обработка исключений помогает обеспечить стабильность работы программы.
'''

'''
Чтобы добавить функционал конвертера валют в наш `AdvancedCalculator`, нам потребуется реализовать методы для конвертации между различными валютами, такими как доллар США (USD), гривна (UAH), польский злотый (PLN), и евро (EUR). Предположим, что у нас есть фиксированные обменные курсы для упрощения. В реальном приложении эти курсы обычно получаются через API финансовых сервисов.
'''

class AdvancedCalculator(SimpleCalculator):
    """
    Класс AdvancedCalculator с функциями калькулятора и конвертера валют.

    Методы:
        Калькуляторные операции.
        convert_currency(amount, from_currency, to_currency): Конвертирует сумму из одной валюты в другую.
    """

    currency_rates = {
        'USD': {'EUR': 0.88, 'UAH': 27.0, 'PLN': 3.8},
        'EUR': {'USD': 1.14, 'UAH': 30.7, 'PLN': 4.32},
        'UAH': {'USD': 0.037, 'EUR': 0.033, 'PLN': 0.14},
        'PLN': {'USD': 0.26, 'EUR': 0.23, 'UAH': 7.1}
    }

    def convert_currency(self, amount, from_currency, to_currency):
        """
        Конвертирует сумму из одной валюты в другую.

        Параметры:
            amount (float): Сумма для конвертации.
            from_currency (str): Исходная валюта.
            to_currency (str): Целевая валюта.

        Возвращает:
            float: Сконвертированная сумма.

        Исключения:
            ValueError: Если валюта не поддерживается.
        """
        if from_currency not in self.currency_rates or to_currency not in self.currency_rates[from_currency]:
            raise ValueError("Unsupported currency conversion.")

        rate = self.currency_rates[from_currency][to_currency]
        return amount * rate

# Пример использования класса с конвертером валют
adv_calc = AdvancedCalculator()
print("100 USD в EUR: ", adv_calc.convert_currency(100, 'USD', 'EUR'))
print("100 EUR в UAH: ", adv_calc.convert_currency(100, 'EUR', 'UAH'))
print("1000 UAH в PLN: ", adv_calc.convert_currency(1000, 'UAH', 'PLN'))


'''
В этом обновлении `AdvancedCalculator`:

1. **Добавление конвертера валют**: 
Мы ввели метод `convert_currency`, 
который позволяет конвертировать сумму из одной валюты в другую.

2. **Таблица обменных курсов**: 
Для упрощения примера используется фиксированный словарь 
`currency_rates` 
с обменными курсами.

3. **Обработка исключений**: 
Добавлена проверка на поддержку валютных пар. 
В случае запроса конвертации с неподдерживаемой валютной 
парой выбрасывается исключение `ValueError`.

Этот пример показывает, 
как можно расширять функциональность класса, 
добавляя новые методы и используя словари для хранения данных, 
таких как валютные курсы. 
В реальном приложении для получения актуальных курсов валют 
обычно используются внешние API.
'''


'''
Для интеграции API ПриватБанка в наш конвертер валют в 
`AdvancedCalculator`, 
нам нужно будет выполнить запрос к API 
для получения актуальных обменных курсов. 
Однако, в рамках текущей сессии у меня нет возможности напрямую взаимодействовать 
с внешними API, 
но я могу показать вам, как это можно реализовать в Python.

Для запросов к API обычно используется библиотека `requests`. 
В нашем случае, мы можем создать метод, 
который будет выполнять GET-запрос к API ПриватБанка, 
извлекать из ответа данные о курсах валют и использовать их для конвертации. 
Вот примерный код:

'''


import requests

class AdvancedCalculator(SimpleCalculator):
    # ... предыдущие методы ...

    def get_currency_rate(self, from_currency, to_currency):
        """
        Получает обменный курс между двумя валютами через API ПриватБанка.

        Параметры:
            from_currency (str): Исходная валюта.
            to_currency (str): Целевая валюта.

        Возвращает:
            float: Обменный курс.

        Исключения:
            ValueError: Если валюта не поддерживается или API недоступно.
        """
        api_url = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            rates = response.json()

            # Найти соответствующий курс валюты
            rate = None
            for item in rates:
                if item['ccy'] == from_currency and item['base_ccy'] == to_currency:
                    rate = float(item['sale'])
                    break

            if rate is None:
                raise ValueError("Currency pair not found.")

            return rate
        except requests.RequestException as e:
            raise ValueError("Error fetching currency rates") from e

    def convert_currency(self, amount, from_currency, to_currency):
        rate = self.get_currency_rate(from_currency, to_currency)
        return amount * rate

# Пример использования
adv_calc = AdvancedCalculator()
try:
    rate = adv_calc.convert_currency(100, 'USD', 'EUR')
    print(f"100 USD в EUR: {rate}")
except ValueError as e:
    print(f"Ошибка: {e}")


'''
Обратите внимание:

1. **GET-запрос к API**: 
Мы используем `requests.get` для выполнения запроса к API ПриватБанка.

2. **Обработка ответа**: 
После получения ответа от API, мы парсим его и ищем нужный обменный курс.

3. **Исключения**: 
Добавлена обработка исключений для сетевых ошибок и ошибок API.

4. **Конвертация валют**: 
Метод `convert_currency` теперь использует актуальные курсы для конвертации.

Для работы этого кода у вас должна быть установлена библиотека `requests`. 
Вы можете установить её, используя `pip install requests`.

'''


'''
Конечно, давайте рассмотрим классы и объекты в Python более подробно, 
особенно сфокусируемся на объектах с собственными атрибутами. 
Когда мы говорим о "собственных атрибутах", 
мы имеем в виду переменные, 
которые связаны с конкретным экземпляром класса. 
Эти атрибуты обычно определяются в методе `__init__`, 
который является конструктором класса.

В качестве примера, 
давайте создадим класс `Car`, 
который будет иметь несколько атрибутов, 
таких как марка, модель и год выпуска. 
Каждый объект класса `Car` будет иметь свои уникальные значения этих атрибутов.
'''


class Car:
    def __init__(self, make, model, year):
        """
        Инициализатор класса Car.

        Параметры:
            make (str): Марка автомобиля.
            model (str): Модель автомобиля.
            year (int): Год выпуска автомобиля.
        """
        self.make = make  # Марка автомобиля
        self.model = model  # Модель автомобиля
        self.year = year  # Год выпуска

    def get_description(self):
        """
        Возвращает описание автомобиля.

        Возвращает:
            str: Описание автомобиля.
        """
        return f"{self.year} {self.make} {self.model}"

# Создание объектов класса Car
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Ford", "Mustang", 2021)

# Вывод информации об автомобилях
print(car1.get_description())  # Выведет: 2020 Toyota Corolla
print(car2.get_description())  # Выведет: 2021 Ford Mustang

'''
В этом примере:

1. **Конструктор `__init__`**: 
Метод `__init__` инициализирует новый экземпляр класса `Car`, 
устанавливая марку (`make`), модель (`model`) и год выпуска (`year`) как атрибуты объекта.

2. **Атрибуты экземпляра**: 
`self.make`, `self.model` и `self.year` являются атрибутами экземпляра. 
Они уникальны для каждого объекта `Car`.

3. **Метод `get_description`**: 
Этот метод возвращает строку с описанием автомобиля, 
используя атрибуты экземпляра.

4. **Создание объектов**: 
`car1` и `car2` являются отдельными объектами класса `Car`, 
каждый со своими уникальными атрибутами.

Этот пример демонстрирует основные принципы работы с классами и объектами в Python, 
включая определение класса, 
создание объектов и использование атрибутов и методов экземпляра.
'''

'''
Отлично! Давайте продолжим изучать объектно-ориентированное программирование в Python, расширяя наш пример с классом `Car`. Мы добавим несколько дополнительных функций, таких как методы для изменения атрибутов, использование приватных атрибутов и создание статических методов в классе.
'''
### Пример: Расширенный Класс `Car`


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._odometer_reading = 0  # Приватный атрибут для пробега

    def get_description(self):
        return f"{self.year} {self.make} {self.model}"

    def read_odometer(self):
        """
        Возвращает пробег автомобиля.

        Возвращает:
            int: Пробег автомобиля.
        """
        return self._odometer_reading

    def update_odometer(self, mileage):
        """
        Обновляет показания одометра автомобиля.

        Параметры:
            mileage (int): Новые показания одометра.
        """
        if mileage >= self._odometer_reading:
            self._odometer_reading = mileage
        else:
            print("Нельзя уменьшить показания одометра!")

    def increment_odometer(self, miles):
        """
        Увеличивает показания одометра на заданное количество миль.

        Параметры:
            miles (int): Количество миль для добавления к текущему пробегу.
        """
        self._odometer_reading += miles

    @staticmethod
    def is_vintage(year):
        """
        Определяет, является ли автомобиль винтажным.

        Параметры:
            year (int): Год выпуска автомобиля.

        Возвращает:
            bool: True, если автомобиль винтажный, иначе False.
        """
        current_year = 2024  # Допустим, текущий год 2024
        return current_year - year >= 25

# Пример использования класса Car
car = Car("Ford", "Mustang", 1967)
print(car.get_description())
print("Винтажный: ", Car.is_vintage(car.year))  # Использование статического метода

# Обновление и чтение одометра
car.update_odometer(50000)
print("Пробег: ", car.read_odometer())

car.increment_odometer(500)
print("Пробег после поездки: ", car.read_odometer())

'''

В этом расширенном классе `Car`:

1. **Приватный атрибут `_odometer_reading`**: 
Используется для хранения пробега автомобиля. 
Префикс `_` указывает, что это внутренний атрибут класса.

2. **Методы `update_odometer` и `increment_odometer`**: 
Эти методы позволяют изменять показания одометра. 

Метод `update_odometer` 
предотвращает уменьшение показаний одометра.

3. **Статический метод `is_vintage`**: 
Этот метод определяет, 
является ли автомобиль винтажным. 
Он не зависит от конкретного экземпляра класса и 
может быть вызван на уровне класса.

Этот пример демонстрирует более продвинутые аспекты 
объектно-ориентированного программирования в Python, 
включая работу с приватными атрибутами, 
методами изменения состояния объекта и использованием статических методов.

'''

