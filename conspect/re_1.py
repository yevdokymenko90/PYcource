'''
Регулярные выражения в Python 
предоставляют мощный способ для поиска 
и манипуляции текстом. 

Они используются для спецификации набора правил, 
которым должны соответствовать строки в тексте, 
что позволяет выполнять сложные поиски и замены в строках.

Python предоставляет модуль `re` 
для работы с регулярными выражениями. 

Вот основные функции и методы, 
предоставляемые этим модулем:

re.search(pattern, string):
Поиск первого вхождения шаблона в строке. 
Возвращает объект `Match` или 
`None`, если совпадение не найдено.

re.match(pattern, string)`: 
Похож на `search`, но ищет совпадение только в начале строки.

re.findall(pattern, string)`: 
Находит все неперекрывающиеся совпадения шаблона в строке и возвращает их в виде списка.

re.finditer(pattern, string)`: 
Похож на `findall`, но возвращает итератор, возвращающий объекты `Match`.

re.sub(pattern, repl, string)`: 
Заменяет все совпадения шаблона в строке на `repl` и возвращает новую строку.
'''


'''
### Примеры Использования Регулярных Выражений

#   Давайте рассмотрим несколько простых примеров использования регулярных выражений в Python.

#### Поиск Всех Электронных Адресов в Тексте
'''

import re

text = "Пожалуйста, свяжитесь с нами по адресу info@example.com или support@example.com."
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

print(emails)

'''
#### Замена Нежелательных Слов в Строке
'''

import re

text = "Этот фильм был ужасен, отвратителен и скучен."
clean_text = re.sub(r"ужасен|отвратителен|скучен", "плох", text)

import re

print(clean_text)

''' Проверка Формата Даты'''

date = "01-01-2020"
if re.match(r'\d{2}-\d{2}-\d{4}', date):
    print("Дата соответствует формату DD-MM-YYYY.")
else:
    print("Дата не соответствует формату DD-MM-YYYY.")




''' Поиск Всех Слов, Начинающихся с Определенной Буквы'''

text = "Кот, картофель, котлета, котик, кот"
words = re.findall(r'\bк\w+', text)


'''
Представленный фрагмент кода на Python использует функцию 
`findall` из модуля `re` 
для поиска всех слов в строке, 
которые начинаются с определенной буквы.

Строка `text` определена как 
"Кот, картофель, котлета, котик, кот". 
Эта строка содержит несколько слов, 
некоторые из которых начинаются с буквы "к".

Затем используется функция 
`re.findall` 
для поиска всех вхождений шаблона в строке `text`. 
Шаблон определен как r'\bк\w+'.

Вот что означает каждая часть шаблона:

- \b - это граница слова. 
Это гарантирует, 
что шаблон совпадает только с теми словами, 
которые начинаются с указанной буквы, 
а не с теми словами, 
которые содержат эту букву в другом месте.

- к - это конкретная буква, с которой должно начинаться каждое слово.

- \w+ совпадает с одним или несколькими символами слова 
(эквивалентно [a-zA-Z0-9_] в английском алфавите). 
Эта часть шаблона гарантирует, 
что совпадает вся слово, 
а не только начальная буква.

Результат функции
re.findall - это список всех слов в `text`, 
которые начинаются с "к". 
Этот список сохраняется в переменной `words`.
'''

'''
Регулярные выражения играют важную роль в автоматизации и автоматизированном тестировании, 
предоставляя гибкие средства для поиска, проверки и манипуляции текстовыми данными. 
В контексте автотестов регулярные выражения могут использоваться для различных задач, 
включая валидацию форматов данных, извлечение информации из логов или ответов сервера и многие другие.
'''

'''
Валидация Форматов Данных

Одно из распространенных применений регулярных выражений в автотестах — 
#валидация форматов данных, таких как электронные адреса, 
номера телефонов, 
идентификаторы и форматы дат. 
Это помогает убедиться, что данные, 
введенные пользователем или возвращенные приложением, 
соответствуют ожидаемым шаблонам.
'''


'''
# Пример: Проверка формата электронной почты**
'''

import re

def validate_email(email):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(pattern, email) is not None

assert validate_email("example@example.com")
assert not validate_email("example.com")

'''
### Извлечение Информации

Регулярные выражения могут использоваться для 
извлечения конкретных частей информации из текстов, 
например, 
из логов приложения или ответов сервера в тестах API. 
Это особенно полезно для анализа сложных текстовых данных 
и проверки наличия или значения определенных данных.
'''


'''
# Пример: Извлечение кодов статуса HTTP из логов**
'''


import re

log = "GET /index.html 200 OK"
match = re.search(r'\b\d{3}\b', log)
if match:
    status_code = match.group(0)
    print("Найденный код статуса HTTP:", status_code)

'''

### Манипуляции с Текстом
'''

''' 
В автотестах часто возникает необходимость модифицировать текстовые данные
для подготовки входных значений или обработки результатов. 
Регулярные выражения предоставляют мощные инструменты для таких манипуляций.
'''


# Замена токенов в строке
import re

url = "https://example.com/api?key=<API_KEY>"
new_url = re.sub(r'<API_KEY>', '123456', url)
print(new_url)

'''

### Поиск Совпадений в Ответах API
'''

'''
При тестировании API можно использовать регулярные выражения для 
проверки наличия определенных данных в ответах, 
например, 
для извлечения токенов доступа или других важных данных, 
которые могут быть использованы в последующих запросах.
'''


#### Пример: Извлечение токена доступа из ответа сервера
import re

response = '{"access_token": "abcd1234", "expires": "3600"}'
token = re.findall(r'"access_token":\s?"(\w+)"', response)
if token:
    print("Токен доступа:", token[0])


'''
Использование регулярных выражений в автоматизации и 
автотестах значительно упрощает работу с текстовыми данными, 
повышая эффективность и надежность тестирования.
'''



'''

Давайте рассмотрим несколько примеров автотестов на Python, 
используя различные подходы и инструменты, 
такие как `unittest` для модульного тестирования 
и `requests` для тестирования API. 
Эти примеры помогут вам понять, 
как можно структурировать тесты для разных сценариев.

### 1. Модульное Тестирование с `unittest`

Модуль 
`unittest` в Python 
предоставляет инструменты для построения тестовых случаев, 
организации тестов в тестовые наборы и их выполнения.

**Пример: Тестирование Функции Сложения**

'''

import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    """
    A test case for the add function.
    """

    def test_add_integers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_floats(self):
        self.assertAlmostEqual(add(1.1, 2.2), 3.3, places=1)

    def test_add_strings_raises_typeerror(self):
        with self.assertRaises(TypeError):
            add('one', 'two')

if __name__ == '__main__':
    unittest.main()

''' 
2. Тестирование API с использованием `requests`
Библиотека 
`requests` 
позволяет легко отправлять HTTP-запросы в Python. 
Она широко используется для тестирования API.

**Пример: 
Тестирование REST API**
'''

import requests
import unittest

class TestUserAPI(unittest.TestCase):
    BASE_URL = "https://jsonplaceholder.typicode.com/users"

    def test_get_user(self):
        user_id = 1
        response = requests.get(f"{self.BASE_URL}/{user_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], user_id)

    def test_user_not_found(self):
        user_id = -1  # Предполагаем, что такого пользователя нет
        response = requests.get(f"{self.BASE_URL}/{user_id}")
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()



    
'''

3. Использование Параметризации Тестов в `pytest`

`pytest` — еще один популярный инструмент для тестирования, 
который поддерживает параметризацию тестов, 
позволяя запускать один и тот же тест с разными входными данными.

**Пример: 
Параметризированный Тест**

'''
import pytest

def multiply(a, b):
    return a * b

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 2),
    (2, 3, 6),
    (4, 5, 20),
    (6, -7, -42),
    (0, 100, 0),
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

'''
Для запуска этого теста потребуется установить 
`pytest` 
и выполнить команду `pytest` в терминале.

Эти примеры демонстрируют разнообразие подходов к автоматизированному тестированию на Python, 
от модульного тестирования внутренней логики приложений до интеграционного тестирования API 
и использования продвинутых функций тестовых фреймворков, 
таких как параметризация тестов в `pytest`.
'''

'''
В контексте автоматизированного тестирования с Playwright, 
регулярные выражения (`re` в Python) 
могут быть использованы для различных целей, 
включая валидацию содержимого веб-страниц, 
обработку и анализ данных, 
полученных в результате тестов, 
и многое другое. 
Playwright позволяет автоматизировать взаимодействие с браузерами, 
а регулярные выражения добавляют гибкость в обработку текстовой информации.

Давайте рассмотрим несколько примеров использования 
`re` в тестах, 
написанных с использованием Playwright.

### Пример 1: 
# Проверка Формата Email на Веб-Странице

Предположим, 
вы хотите убедиться, 
что на веб-странице отображается корректный email. 
В этом примере мы сначала получаем текст с веб-страницы, 
а затем проверяем его на соответствие шаблону email с использованием `re`.

'''
from playwright.sync_api import sync_playwright
import re

def test_email_format():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://example.com/contact')

        # Предполагаем, что email находится в элементе с идентификатором 'email'
        email_text = page.text_content('#email')
        assert re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email_text), "Email не соответствует ожидаемому формату"

        browser.close()

'''
# Это пример и не будет запускаться как реальный тест без соответствующей настройки окружения и URL.
'''
'''
### Пример 2: Извлечение Информации из Страницы
'''
'''
Предположим, 
вам нужно извлечь определенные данные, 
например, 
идентификаторы из URL, 
указанных на странице. 
Сначала вы получаете HTML-контент страницы, 
а затем используете регулярные выражения для извлечения нужной информации.
'''

from playwright.sync_api import sync_playwright
import re

def extract_ids_from_links():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://example.com/items')

        # Получаем все ссылки на странице
        links = page.query_selector_all('a')
        ids = []

        for link in links:
            href = link.get_attribute('href')
            match = re.search(r'/item/(\d+)', href)
            if match:
                ids.append(match.group(1))

        print(ids)  # Выводим список идентификаторов
        browser.close()
        
'''
# Это пример и не будет запускаться как реальный тест без соответствующей настройки окружения и URL.
'''

'''
Эти примеры иллюстрируют, 
как регулярные выражения могут быть интегрированы в тесты Playwright 
для выполнения сложных задач поиска и 
анализа данных на веб-страницах. 
Использование `re` в сочетании с возможностями Playwright 
открывает широкие возможности для автоматизации тестирования веб-приложений.
'''


'''
В текущем контексте выполнения кода и демонстрации примеров, 
я не могу напрямую выполнять запросы к веб-страницам или 
интерпретировать результаты работы Playwright, 
но я могу предложить еще несколько идей о том, 
как можно использовать регулярные выражения 
(`re`) 
вместе с Playwright для различных сценариев тестирования:
'''

'''
### Пример 3: 
# Проверка URL на Соответствие Ожидаемому Шаблону
'''

'''
Предположим, вы тестируете веб-приложение, где после выполнения определенного действия ожидается переход на URL, соответствующий определенному шаблону.
'''


'''
# Предполагаемый код, требующий наличия среды Playwright
'''

import re

def test_navigation_url(page):
    # Выполнение действия, после которого ожидается переход
    page.click("text='Подробнее о продукте'")
    page.wait_for_load_state('networkidle')

    current_url = page.url
    assert re.match(r'https://example.com/product/\d+', current_url), "URL не соответствует ожидаемому шаблону"

'''
### Пример 4: Валидация Формата Даты в Ответе
'''
'''
Если ваше приложение отображает даты в определенном формате, вы можете проверить соответствие этого формата ожидаемому, используя регулярные выражения.
'''
'''
Предполагаемый код, требующий наличия среды Playwright
'''
import re

def test_date_format(page):
    page.goto("https://example.com/events")
    date_text = page.text_content(".event-date")

    assert re.match(r'\d{2}/\d{2}/\d{4}', date_text), "Формат даты не соответствует 'ДД/ММ/ГГГГ'"

'''
### Пример 5: Извлечение и Проверка Данных из Таблицы
'''

'''
Допустим, 
вам нужно проверить, 
что определенные данные присутствуют в таблице на веб-странице. 
Сначала вы извлекаете данные, 
а затем используете регулярные выражения для их анализа.
'''

'''
Предполагаемый код, требующий наличия среды Playwright
'''

import re

def test_data_in_table(page):
    page.goto("https://example.com/report")
    table_data = page.text_content("#report-table")
    expected_data = "Имя: John, Возраст: 30, Город: New York"

    assert re.search(r'Имя: \w+, Возраст: \d+, Город: \w+', table_data), "Данные не найдены в таблице"

'''
Эти примеры демонстрируют гибкость использования регулярных выражений 
для удовлетворения разнообразных потребностей 
в тестировании веб-приложений с Playwright. 
Регулярные выражения позволяют легко анализировать и 
проверять текстовые данные, 
извлекаемые в ходе автоматизированных тестов, 
упрощая тем самым процесс подтверждения соответствия приложения 
его функциональным требованиям и спецификациям.
'''
