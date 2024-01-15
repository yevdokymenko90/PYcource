"""
Примеры Лямбда-Функций в Python
Лямбда-функции в Python — это небольшие анонимные функции, 
состоящие из одного выражения. Они часто используются в ситуациях, 
где необходима простая функция для кратковременного использования. 
Лямбда-функции ограничены одним выражением, 
что значит, 
что они не могут содержать множество операторов или ветвлений, 
как стандартные функции. 
Обычно их используют в качестве аргумента для функций высшего порядка, 
таких как map(), filter() и sorted().

Основной Синтаксис
Синтаксис лямбда-функции:

python
Copy code
lambda arguments: expression
arguments — это список аргументов, которые функция принимает (как в обычной функции).
expression — это выражение, использующее эти аргументы.
Примеры Использования Лямбда-Функций
Давайте рассмотрим несколько примеров лямбда-функций с подробными комментариями:

"""

# Пример 1: Лямбда-функция для сложения двух чисел
add = lambda x, y: x + y
result = add(5, 3)  # result = 8
print("Сумма 5 и 3:", result)

# Пример 2: Использование лямбда-функции в качестве аргумента функции map
nums = [1, 2, 3, 4, 5]
squared_nums = list(map(lambda x: x**2, nums))  # Возводит каждое число в квадрат
print("Квадраты чисел:", squared_nums)

# Пример 3: Использование лямбда-функции в качестве аргумента функции filter
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = list(filter(lambda x: x % 2 == 0, nums))  # Фильтрует четные числа
print("Четные числа:", even_nums)

# Пример 4: Использование лямбда-функции в качестве аргумента функции sorted
words = ["apple", "banana"]


from playwright.sync_api import sync_playwright

def test_element_presence_with_lambda():
    """
    Тестирование наличия элемента на странице с использованием лямбда-функций.
    """

    with sync_playwright() as p:
        # Запуск браузера
        browser = p.chromium.launch()
        page = browser.new_page()

        # Открытие тестовой страницы
        page.goto('https://example.com')

        # Проверка наличия заголовка на странице с использованием лямбда-функции
        assert (lambda: 'Example Domain' in page.text_content('h1'))()

        # Закрытие браузера
        browser.close()

if __name__ == "__main__":test_element_presence_with_lambda()






### Объяснение Кода
'''
1. **Импорт необходимых модулей:**
   - Мы начинаем с импорта `sync_playwright` из `playwright.sync_api`. 
   Это позволит нам использовать синхронные версии методов Playwright для управления браузером.

2. **Определение тестовой функции:**
   - Функция `test_element_presence_with_lambda` объявлена для выполнения нашего теста.

3. **Запуск сессии Playwright:**
   - В контекстном менеджере `with sync_playwright() as p` 
   мы инициализируем Playwright и получаем объект для работы с браузером.

4. **Запуск браузера:**
   - `browser = p.chromium.launch()` запускает браузер Chromium.

5. **Открытие новой страницы:**
   - `page = browser.new_page()` открывает новую вкладку или страницу в браузере.

6. **Переход на тестовую страницу:**
   - `page.goto('https://example.com')` перенаправляет браузер на указанный URL.

7. **Проверка наличия элемента с использованием лямбда-функции:**
   - `assert (lambda: 'Example Domain' in page.text_content('h1'))()` — это лямбда-функция, 
   которая извлекает текст из элемента `h1` и проверяет, содержит ли он строку `'Example Domain'`. 
   Использование `assert` гарантирует, что тест будет неудачным, если условие не выполнено.

8. **Закрытие браузера:**
   - После выполнения проверки браузер закрывается командой `browser.close()`.

9. **Запуск теста:**
   - Блок `if __name__ == "__main__":` позволяет запустить функцию теста, если скрипт выполняется как основная программа.

Этот скрипт демонстрирует, как лямбда-функции могут быть использованы в тестах Playwright для создания кратких и эффективных проверок. 
Лямбда-функции особенно полезны для создания простых анонимных функций на лету, что делает код более компактным и читаемым.

''' 

def greeting(greet): 
    return lambda name : f"{greet},{name}!"


morning_greeting = greeting("Good Morning")

print(morning_greeting("Dimon"))
# Good Morning, Dimon!

evening_greeting = greeting("Good Evening")

print(evening_greeting("Dimon"))
# Good Evening, Dimon!

'''
The active selection is a Python script that demonstrates 
the use of higher-order functions and 
lambda functions to create customized greeting messages.

The `greeting` function is a higher-order function, 
which means it's a function that returns another function. 
In this case, it returns a lambda function. 
The `greeting` function takes one argument, `greet`, 
which is a string that represents the type of greeting (e.g., "Good Morning" or "Good Evening").

The lambda function it returns takes one argument, `name`, 
and returns a formatted string that combines the greeting and the name. 
The `f"{greet},{name}!"` is an f-string, 
a feature in Python that allows for embedded expressions inside string literals. 
The `{greet}` and `{name}` inside the f-string are placeholders that get replaced by the values of `greet` and `name`.

The `morning_greeting` and `evening_greeting` 
are instances of the lambda function returned by the `greeting` function. 
When you call `morning_greeting("Dimon")` or `evening_greeting("Dimon")`, 
it's equivalent to calling the lambda function with "Dimon" as the argument for `name`.

The `print` function is a built-in Python function that writes the specified message to the screen, 
or other standard output device. 
The message can be a string, or any other object, 
the object will be converted into a string before written to the screen. 
In this case, it's used to print the result of the 
`morning_greeting` and `evening_greeting` function calls to the console.


Активный выбор - это скрипт на Python, 
который демонстрирует использование функций высшего порядка и 
лямбда-функций для создания настраиваемых приветственных сообщений.

Функция `greeting` - это функция высшего порядка, 
что означает, что это функция, 
которая возвращает другую функцию. 
В данном случае она возвращает лямбда-функцию. 
Функция `greeting` принимает один аргумент, `greet`, 
который является строкой, 
представляющей тип приветствия (например, "Good Morning" или "Good Evening").

Возвращаемая ею лямбда-функция принимает один аргумент, `name`, 
и возвращает отформатированную строку, 
которая объединяет приветствие и имя. 
`f"{greet},{name}!"` - это f-строка, 
функция в Python, 
которая позволяет встраивать выражения внутри строковых литералов. 
`{greet}` и `{name}` внутри f-строки - 
это заполнители, которые заменяются значениями `greet` и `name`.

`morning_greeting` и `evening_greeting` - 
это экземпляры лямбда-функции, возвращаемой функцией `greeting`. 
Когда вы вызываете `morning_greeting("Dimon")` или `evening_greeting("Dimon")`, 
это эквивалентно вызову лямбда-функции с "Dimon" в качестве аргумента для `name`.

Функция `print` - это встроенная функция Python, 
которая записывает указанное сообщение на экран 
или другое стандартное устройство вывода. 
Сообщение может быть строкой или любым другим объектом, 
объект будет преобразован в строку перед записью на экран. 
В данном случае она используется для 
вывода результата вызовов функций 
`morning_greeting` и `evening_greeting` в консоль.
'''
