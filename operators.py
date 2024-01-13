'''
Унарные операторы в программировании – это операторы, 
которые применяются только к одному операнду. 
В Python, основными унарными операторами являются унарный минус (-), 
который меняет знак числа, и унарный плюс (+), который оставляет число без изменений. 
Также сюда можно отнести логическое отрицание (not).
'''


# Унарный минус и унарный плюс
num = 5
neg_num = -num  # Унарный минус, меняет знак числа
pos_num = +num  # Унарный плюс, оставляет число без изменений

print("Исходное число:", num)         # Вывод: Исходное число: 5
print("С унарным минусом:", neg_num)  # Вывод: С унарным минусом: -5
print("С унарным плюсом:", pos_num)   # Вывод: С унарным плюсом: 5

# Логическое отрицание (not)
bool_val = True
negated_bool_val = not bool_val  # Инвертирует значение

print("Исходное логическое значение:", bool_val)          # Вывод: Исходное логическое значение: True
print("Инвертированное логическое значение:", negated_bool_val)  # Вывод: Инвертированное логическое значение: False

'''
Пошаговые Объяснения:
Унарный Минус (-):

neg_num = -num применяет унарный минус к num. 
Это меняет знак числа num на противоположный, из положительного в отрицательное.
Унарный Плюс (+):

pos_num = +num применяет унарный плюс к num. 
Это оставляет число без изменений. 
Унарный плюс чаще всего используется для улучшения читаемости кода, 
чтобы явно указать на положительное значение.
Логическое Отрицание (not):

negated_bool_val = not bool_val применяет логическое отрицание к bool_val. 
Оператор not инвертирует логическое значение – True становится False, и наоборот.
Эти унарные операторы часто используются в различных сценариях программирования 
для изменения знака чисел или инвертирования логических значений. 
Они являются важными элементами языка Python и могут значительно влиять на поведение программы.
'''



'''
Унарные операторы в автотестах чаще всего используются для логических проверок или условий. 
Например, унарное отрицание (not) может использоваться для проверки, 
что определенный элемент не отображается на странице, или что какое-то условие не выполняется. 
Рассмотрим пример автотеста с использованием Python и библиотеки Selenium, где мы применим унарные операторы:

Пример: Использование Унарных Операторов в Автотестах
'''


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Настройка веб-драйвера
driver = webdriver.Chrome()
driver.get("https://example.com")

# Проверка наличия элемента на странице
try:
    element = driver.find_element_by_id("unique-element-id")
    element_found = True
except NoSuchElementException:
    element_found = False

# Использование унарного оператора not для проверки отсутствия элемента
if not element_found:
    print("Элемент не найден на странице.")
else:
    print("Элемент найден.")

# Закрытие браузера после теста
driver.quit()


'''
Пошаговые Объяснения:

Настройка WebDriver:
Используется Selenium WebDriver для открытия браузера и перехода на заданный URL.

Поиск Элемента:
Происходит попытка найти элемент на странице по его уникальному идентификатору.

Обработка Исключения:
Если элемент не найден, генерируется исключение NoSuchElementException. 
В этом случае переменная element_found устанавливается в False.

Применение Унарного Оператора:
Используется унарный оператор not для проверки, что элемент отсутствует на странице. 
Это полезно, например, для проверки, 
что пользователь не авторизован 
(если элемент является частью пользовательского интерфейса для авторизованных пользователей).
Этот пример иллюстрирует, 
как унарный оператор not может быть использован в автотестах для проверки отрицательных условий, 
например, отсутствия элемента на веб-странице. 
Это очень распространенная практика в автоматизированном тестировании, 
позволяющая убедиться, что UI отвечает ожиданиям в различных сценариях.

'''

'''
Бинарные операторы в программировании применяются к двум операндам и 
выполняют различные математические, логические или сравнительные операции. 
В Python к бинарным операторам относятся арифметические операторы 
(например, +, -, *, /), операторы сравнения (например, ==, !=, >, <), 
а также логические операторы (and, or).
Пример: Использование Бинарных Операторов в Python
'''

# Арифметические операторы
a = 10
b = 5

addition = a + b  # Сложение
subtraction = a - b  # Вычитание
multiplication = a * b  # Умножение
division = a / b  # Деление

print("Сложение:", addition)
print("Вычитание:", subtraction)
print("Умножение:", multiplication)
print("Деление:", division)

# Операторы сравнения
equals = a == b  # Равенство
not_equals = a != b  # Неравенство
greater_than = a > b  # Больше
less_than = a < b  # Меньше

print("Равенство:", equals)
print("Неравенство:", not_equals)
print("Больше:", greater_than)
print("Меньше:", less_than)

# Логические операторы
logical_and = (a > 5) and (b < 10)  # Логическое И
logical_or = (a < 5) or (b < 10)  # Логическое ИЛИ

print("Логическое И:", logical_and)
print("Логическое ИЛИ:", logical_or)


'''
Пошаговые Объяснения:

Арифметические Операторы:
Сложение (+), вычитание (-), умножение (*), и деление (/) являются бинарными операторами, 
так как они применяются к двум операндам (a и b).
Операторы Сравнения:

Операторы равенства (==) и неравенства (!=), 
а также операторы сравнения (>, <) также являются бинарными, 
так как они сравнивают два значения.

Логические Операторы:
and и or - бинарные логические операторы. 
Они применяются к двум логическим выражениям и возвращают 
True или False в зависимости от значений этих выражений.

Эти операторы широко используются в программировании 
для выполнения математических операций, 
сравнения значений и объединения логических условий. 
Они являются основой для многих расчетов и алгоритмов в любом виде программного обеспечения.
'''




'''
Бинарные операторы в автотестах часто используются для сравнения значений, 
полученных в результате тестирования, 
с ожидаемыми значениями, 
а также для создания сложных логических условий. 
Давайте рассмотрим пример автотеста, используя Python и Selenium, 
где мы применим бинарные операторы для проверки элементов на веб-странице.
Пример: Использование Бинарных Операторов в Автотестах
'''

from selenium import webdriver

# Настройка веб-драйвера
driver = webdriver.Chrome()
driver.get("https://example.com")

# Поиск элементов на странице
element1 = driver.find_element_by_id("element1")
element2 = driver.find_element_by_id("element2")

# Получение текста из элементов
text1 = element1.text
text2 = element2.text

# Использование бинарных операторов для сравнения текста элементов
# Операторы сравнения
texts_are_equal = text1 == text2  # Равенство
texts_are_not_equal = text1 != text2  # Неравенство

print("Тексты элементов равны:", texts_are_equal)
print("Тексты элементов не равны:", texts_are_not_equal)

# Проверка длины текста элементов
# Операторы сравнения и арифметические операторы
length_condition = (len(text1) > 5) and (len(text2) < 10)

print("Длина текста element1 больше 5 и длина текста element2 меньше 10:", length_condition)

# Закрытие браузера после теста
driver.quit()


'''
Пошаговые Объяснения:
Настройка WebDriver:

Используется Selenium WebDriver для открытия браузера и перехода на заданный URL.
Поиск и Получение Текста Элементов:

Находятся элементы на странице и извлекается их текст.

Операторы Сравнения:
- Используется оператор равенства (==) и неравенства (!=) для сравнения текста двух элементов.

Сложные Логические Условия:
- Используются арифметические операторы (len(text)) 
- в сочетании с логическими операторами (and) 
для создания сложного условия, проверяющего длину текста элементов.

Этот пример иллюстрирует, 
как бинарные операторы могут быть использованы в автотестах для выполнения проверок, 
основанных на сравнении или логических условиях. 
Они являются важной частью автоматизации тестирования, 
помогая проверять различные аспекты веб-приложения и обеспечивая точность тестовых сценариев.
'''





'''
Инфиксная запись – это способ записи математических и логических формул, 
при котором операторы располагаются между операндами. 
В большинстве языков программирования, включая Python, 
именно инфиксная запись используется для выражения арифметических операций, 
сравнений и логических операций.

Особенности Инфиксной Записи:
- Читаемость: Инфиксная запись является интуитивно понятной, 
так как она близка к обычному математическому представлению операций.
- Порядок Операций: Важно учитывать порядок выполнения операций, 
который в большинстве случаев соответствует математическим правилам 
(например, умножение и деление выполняются до сложения и вычитания).

Пример: Инфиксная Запись в Python
'''


# Примеры арифметических операций
a = 5
b = 2

# Сложение
addition = a + b

# Вычитание
subtraction = a - b

# Умножение
multiplication = a * b

# Деление
division = a / b

print("Сложение:", addition)
print("Вычитание:", subtraction)
print("Умножение:", multiplication)
print("Деление:", division)

# Примеры операций сравнения
equals = a == b  # Равенство
greater_than = a > b  # Больше

print("Равенство:", equals)
print("Больше:", greater_than)

# Примеры логических операций
c = True
d = False

logical_and = c and d  # Логическое 'И'
logical_or = c or d  # Логическое 'ИЛИ'

print("Логическое 'И':", logical_and)
print("Логическое 'ИЛИ':", logical_or)


'''
Пошаговые Объяснения:
Арифметические Операции:

Используются основные арифметические операторы (+, -, *, /), где операторы располагаются между операндами (инфиксная запись).
Операции Сравнения:

Примеры сравнения двух переменных (==, >), также использующие инфиксную запись.
Логические Операции:

Инфиксные логические операторы and и or, применяемые к двум логическим значениям.
Во всех этих случаях инфиксная запись обеспечивает читаемость и понятность кода, 
что является стандартом в большинстве языков программирования, включая Python. 
Это подход соответствует традиционному математическому способу записи выражений, 
делая программный код доступным для понимания широкой аудитории.
'''



'''
В контексте автотестов, 
особенно при использовании таких инструментов как Selenium с Python, 
инфиксная запись часто используется для сравнения ожидаемых результатов с фактическими, 
а также для формирования сложных условий в логических выражениях. 
Давайте рассмотрим пример автотеста, 
в котором мы будем использовать инфиксную запись для проверки различных условий на веб-странице.

Пример: Инфиксная Запись в Автотестах
'''

from selenium import webdriver

# Инициализация веб-драйвера и открытие страницы
driver = webdriver.Chrome()
driver.get("https://example.com")

# Поиск элементов на странице и получение их свойств
element1 = driver.find_element_by_id("element1")
element2 = driver.find_element_by_id("element2")

element1_text = element1.text
element2_text = element2.text

# Пример использования инфиксных операторов сравнения
# Проверка равенства текстов элементов
texts_are_equal = element1_text == element2_text

# Пример использования инфиксных логических операторов
# Проверка, что текст одного элемента не пустой и тексты элементов не равны
valid_condition = (element1_text != "") and (element1_text != element2_text)

print("Тексты элементов равны:", texts_are_equal)
print("Проверка валидности:", valid_condition)

# Закрытие веб-драйвера
driver.quit()


'''
Пошаговые Объяснения:
Инициализация WebDriver и Открытие Страницы:

Используется Selenium WebDriver для открытия браузера и перехода на заданный URL.
Получение Текста Элементов:

Находятся элементы на странице и извлекается их текст.
Инфиксные Операторы Сравнения:

Используется оператор равенства (==) для сравнения текста двух элементов.
Инфиксные Логические Операторы:

Используется комбинация инфиксных логических операторов != (неравенство) 
и and для создания сложного условия, которое проверяет, 
что текст одного из элементов не пустой и тексты элементов не равны друг другу.
Этот пример иллюстрирует, 
как инфиксная запись используется в автотестах для формирования условий и сравнений. 
Это позволяет выполнять точные и понятные проверки в автоматизированных тестах, 
обеспечивая надежность и читаемость кода тестов.
'''


#Давайте последовательно выполним каждый из заданных шагов.

#Шаг 1: Создание Переменных с Одинаковыми Множествами

# Создание двух переменных с одинаковыми множествами
set1 = {1, 2, 3}
set2 = {1, 2, 3}
#Здесь set1 и set2 являются двумя разными объектами, но оба содержат одинаковые элементы.

#Шаг 2: Сравнение Объектов

# Сравнение двух множеств
comparison_result = set1 == set2
print("Результат сравнения set1 и set2:", comparison_result)
#Это сравнение проверяет, содержат ли set1 и set2 одни и те же элементы. 
#Поскольку оба множества содержат одинаковые элементы, результат будет True.

#Шаг 3: Сравнение Идентичности Объектов

# Сравнение идентичности объектов
identity_result = set1 is set2
print("Результат сравнения идентичности set1 и set2:", identity_result)
#Оператор is сравнивает идентичность объектов, т.е. являются ли set1 и set2 одним и тем же объектом в памяти. 
#В данном случае, хотя содержимое set1 и set2 одинаково, они являются разными объектами, поэтому результат будет False.

#Шаг 4: Проверка Наличия Элементов
#python

# Проверка наличия элемента в множестве
element_in_set1 = 1 in set1
element_in_set2 = 4 in set2

print("Элемент 1 в set1:", element_in_set1)
print("Элемент 4 в set2:", element_in_set2)
#Здесь мы проверяем наличие элементов в множествах с помощью оператора in. 
#В set1 есть элемент 1, так что результат будет True. В set2 нет элемента 4, поэтому результат будет False.





# Шаг 1: Создание двух переменных с одинаковыми множествами (sets)
# Оба множества содержат одни и те же элементы: 1, 2 и 3.
set1 = {1, 2, 3}
set2 = {1, 2, 3}

# Шаг 2: Сравнение двух множеств на равенство содержимого
# Оператор == сравнивает, содержат ли set1 и set2 одинаковые элементы.
# Так как элементы в set1 и set2 одинаковые, результат будет True.
comparison_result = set1 == set2
print("Результат сравнения set1 и set2:", comparison_result)  # Выведет: True

# Шаг 3: Сравнение идентичности объектов
# Оператор is проверяет, являются ли set1 и set2 одним и тем же объектом в памяти.
# Несмотря на одинаковое содержимое, set1 и set2 являются разными объектами.
# Следовательно, результат будет False.
identity_result = set1 is set2
print("Результат сравнения идентичности set1 и set2:", identity_result)  # Выведет: False

# Шаг 4: Проверка наличия элементов в множестве
# Оператор in используется для проверки, содержится ли элемент в множестве.
# Проверяем, содержится ли элемент 1 в set1 (ожидаемый результат True).
# Проверяем, содержится ли элемент 4 в set2 (ожидаемый результат False).
element_in_set1 = 1 in set1
element_in_set2 = 4 in set2

print("Элемент 1 в set1:", element_in_set1)  # Выведет: True
print("Элемент 4 в set2:", element_in_set2)  # Выведет: False


