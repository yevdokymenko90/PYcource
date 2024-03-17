#if in func
'''
Использование инструкции if внутри функций в Python является мощным инструментом для 
контроля потока выполнения программы на основе различных условий. 
Функция может изменять своё поведение в зависимости от входных данных или других условий. 
Ниже представлен пример использования if в функциях с подробными комментариями и документацией. 
'''

"""
Пример использования инструкции if в функциях в Python.

Этот скрипт содержит функцию, которая ведет себя по-разному в зависимости от переданных в нее аргументов.
"""

def calculate_price(item, discount):
    """
    Рассчитывает итоговую цену товара с учетом скидки.

    :param item: Словарь с информацией о товаре, включая 'name' (название) и 'price' (цена).
    :param discount: Процент скидки на товар.
    :return: Итоговая цена товара с учетом скидки.
    """
    # Проверка, применима ли скидка к товару
    if discount > 0 and item['price'] > 20:
        return item['price'] * (1 - discount / 100)
    else:
        # Если скидка не применима, возвращается полная цена
        return item['price']

# Пример использования функции
item = {'name': 'Чашка', 'price': 25}
discount = 10

final_price = calculate_price(item, discount)
print(f"Итоговая цена товара {item['name']}: {final_price}")
# Выведет: Итоговая цена товара Чашка: 22.5

"""
В этом коде:
1. Функция 'calculate_price' принимает два аргумента: 'item' и 'discount'.
2. Используется инструкция if для проверки, применима ли скидка к товару.
3. Если условие выполняется (скидка больше 0 и цена товара выше 20), цена уменьшается на процент скидки.
4. Если условие не выполняется, возвращается полная цена товара без скидки.

Этот код демонстрирует, 
как можно использовать условные конструкции внутри функций для 
реализации различной логики в зависимости от условий. 
В этом примере, 
в зависимости от размера скидки и цены товара, 
функция рассчитывает итоговую цену с учетом скидки или без неё. 
Это позволяет сделать функцию гибкой и адаптивной к разным ситуациям, 
что является важным аспектом в разработке программного обеспечения.

Такой подход повышает переиспользуемость кода и облегчает его тестирование и поддержку, 
поскольку логика, 
связанная с определенными условиями, 
централизованно управляется внутри одной функции.

"""


'''

создай функцию route_info которой будет передаваться словарь, 
если в словаре есть ключ distance и его значение - целое число, 
верните строку "Distance to your destination is <distance>" 
иначе если в словаре есть ключи speed  и time 
верни строку "Distance to your destination is < speed * time>"  
иначе верни строку "No distance info is available"  
вызови функцию несколько раз с разными аргументами 

Давайте создадим функцию route_info, 
которая обрабатывает словарь и 
возвращает информацию о расстоянии 
в зависимости от предоставленных данных. 
Функция будет проверять наличие и тип данных ключей в словаре, 
выполняя различные действия в соответствии с условиями.

'''

def route_info(data):
    """
    Возвращает информацию о расстоянии до пункта назначения.

    :param data: Словарь с информацией о маршруте.
    :return: Строка с описанием расстояния до пункта назначения.
    """
    # Проверка наличия ключа 'distance' и его типа
    if 'distance' in data and isinstance(data['distance'], int):
        return f"Distance to your destination is {data['distance']} km."

    # Проверка наличия ключей 'speed' и 'time'
    elif 'speed' in data and 'time' in data:
        # Расчет расстояния на основе скорости и времени
        distance = data['speed'] * data['time']
        return f"Distance to your destination is {distance} km."

    # Если ни одно из условий не выполняется
    else:
        return "No distance info is available."

# Примеры вызова функции с разными аргументами

# Словарь с ключом 'distance'
print(route_info({'distance': 120}))
# Выведет: Distance to your destination is 120 km.

# Словарь с ключами 'speed' и 'time'
print(route_info({'speed': 60, 'time': 2}))
# Выведет: Distance to your destination is 120 km.

# Словарь без необходимой информации
print(route_info({'weather': 'sunny'}))
# Выведет: No distance info is available.


'''

Объяснение Кода
Функция route_info принимает один аргумент data, который является словарем.
Сначала проверяется, 
содержит ли словарь ключ distance и является ли его значение целым числом. 
Если условие истинно, возвращается соответствующая строка.
Если первое условие не выполняется, 
проверяется наличие ключей speed и time. 
Если они есть, рассчитывается расстояние и возвращается соответствующая строка.
Если ни одно из условий не выполняется, 
возвращается строка, 
указывающая на отсутствие информации о расстоянии.
Эта функция демонстрирует использование if-elif-else 
для обработки различных случаев входных данных 
и может быть применена в различных сценариях, 
где требуется обработка словаря с разнообразными данными.

'''

'''

Конечно, вот альтернативный способ решения этой задачи. 
В этом примере мы используем метод .get() словаря, 
который позволяет нам избежать исключения, 
если ключ отсутствует в словаре. 
Метод .get() возвращает None по умолчанию, 
если ключ не найден, что позволяет нам элегантно обрабатывать отсутствующие данные.

Альтернативное Решение

'''


def route_info_alt(data):
    """
    Возвращает информацию о расстоянии до пункта назначения.

    Использует метод .get() словаря для более удобной обработки отсутствующих ключей.

    :param data: Словарь с информацией о маршруте.
    :return: Строка с описанием расстояния до пункта назначения.
    """
    distance = data.get('distance')
    speed = data.get('speed')
    time = data.get('time')

    # Проверка и расчет на основе полученных значений
    if isinstance(distance, int):
        return f"Distance to your destination is {distance} km."
    elif speed is not None and time is not None:
        calculated_distance = speed * time
        return f"Distance to your destination is {calculated_distance} km."
    else:
        return "No distance info is available."

# Примеры вызова функции с разными аргументами

print(route_info_alt({'distance': 120}))  # Distance to your destination is 120 km.
print(route_info_alt({'speed': 60, 'time': 2}))  # Distance to your destination is 120 km.
print(route_info_alt({'weather': 'sunny'}))  # No distance info is available.


'''

Объяснение Кода
Функция route_info_alt сначала извлекает значения для ключей distance, speed и time, 
используя метод .get(). 
Если ключ отсутствует, метод возвращает None.
После этого функция проверяет, 
является ли значение distance целым числом. 
Если да, возвращается соответствующая строка.
Если distance не является целым числом, 
функция проверяет, не равны ли None значения speed и time. 
Если оба значения присутствуют, 
расстояние рассчитывается и возвращается соответствующая строка.
Если ни одно из этих условий не выполняется, 
возвращается сообщение об отсутствии информации.
Этот подход позволяет обрабатывать отсутствующие ключи более гибко, 
избегая возникновения исключения KeyError при попытке доступа к несуществующему ключу.

'''


def route_info(route):
    if ('distance' in route) and (type(route['distance']) == int):
        return f"Distance to your destination is {route['distance']} km."
    
    if ('speed' in route) and ('time' in route):
        return f"Distance to your destination is {route['speed'] * route['time']} km."
    
    return "No distance info is available."

    
print(route_info({'distance': 15}))

print(route_info({'distance': '15'}))

print(route_info({}))

print(route_info({'speed': 60, 'time': 2}))
            
print(route_info({'my_speed': 60}))     

'''


Предоставленный Python скрипт определяет функцию `route_info(route)`, 
которая вычисляет и возвращает расстояние до пункта назначения на основе информации, 
предоставленной в словаре `route`.

Функция `route_info(route)` принимает словарь `route` в качестве аргумента. 
Этот словарь может содержать ключи, такие как 'distance', 'speed' и 'time'.

Сначала функция проверяет, 
присутствует ли ключ 'distance' в словаре 
и является ли его значение целым числом. 
Если это условие выполняется, она возвращает строку, 
указывающую расстояние до пункта назначения в километрах.

Если ключ 'distance' отсутствует или 
его значение не является целым числом, 
функция затем проверяет, 
присутствуют ли в словаре ключи 'speed' и 'time'. 
Если они есть, она вычисляет расстояние, 
умножая значения скорости и времени, и возвращает строку, 
указывающую вычисленное расстояние до пункта назначения.

Если ни одно из вышеуказанных условий не выполняется, 
функция возвращает строку, указывающую, 
что информация о расстоянии недоступна.

Затем скрипт вызывает функцию `route_info(route)` 
с разными словарями и выводит возвращаемую информацию о расстоянии. 
Словари, используемые в вызовах функции, 
отличаются содержащимися в них ключами и значениями, 
что демонстрирует, 
как функция обрабатывает разные входные данные.


The provided Python script defines a function `route_info(route)` 
that calculates and returns the distance to 
a destination based on the information provided in the `route` dictionary.

The function `route_info(route)` takes a dictionary `route` as an argument. 
This dictionary can contain keys such as 'distance', 'speed', and 'time'. 

The function first checks if the 'distance' key is present 
in the dictionary and if its value is an integer. 
If this condition is met, 
it returns a string indicating the distance to the destination in kilometers.

If the 'distance' key is not present or its value is not an integer, 
the function then checks if both 'speed' and 'time' keys are present in the dictionary. 
If they are, 
it calculates the distance by multiplying the speed and time values 
and returns a string indicating the calculated distance to the destination.

If neither of the above conditions are met, 
the function returns a string stating that no distance information is available.

The script then calls the `route_info(route)` 
function with different dictionaries and prints the returned distance information. 
The dictionaries used in the function calls vary in the keys and values they contain, demonstrating how the function handles different inputs.

'''


def route_info(route):
    """
    Определяет расстояние до пункта назначения на основе данных маршрута.

    Функция анализирует переданный словарь `route` и возвращает информацию о расстоянии.
    Если в словаре есть ключ 'distance' с целочисленным значением, возвращается соответствующая строка.
    Если в словаре есть ключи 'speed' и 'time', расстояние вычисляется на их основе.
    Если ни одно из условий не выполняется, возвращается строка об отсутствии информации.

    :param route: Словарь с информацией о маршруте.
    :return: Строка с информацией о расстоянии.
    """

    # Проверка наличия ключа 'distance' и его типа
    if ('distance' in route) and (type(route['distance']) == int):
        # Возвращается расстояние, если ключ 'distance' присутствует и его значение - целое число
        return f"Distance to your destination is {route['distance']} km."
    
    # Проверка наличия ключей 'speed' и 'time'
    if ('speed' in route) and ('time' in route):
        # Вычисляется и возвращается расстояние на основе скорости и времени
        return f"Distance to your destination is {route['speed'] * route['time']} km."
    
    # Возвращается сообщение об отсутствии информации, если ни одно из условий не выполняется
    return "No distance info is available."

# Примеры вызова функции с разными аргументами

# Словарь с ключом 'distance' и целочисленным значением
print(route_info({'distance': 15}))  # Выведет: Distance to your destination is 15 km.

# Словарь с ключом 'distance', но значением не целого типа
print(route_info({'distance': '15'}))  # Выведет: No distance info is available.

# Пустой словарь, не содержащий необходимых ключей
print(route_info({}))  # Выведет: No distance info is available.

# Словарь с ключами 'speed' и 'time'
print(route_info({'speed': 60, 'time': 2}))  # Выведет: Distance to your destination is 120 km.

# Словарь без ключей 'distance', 'speed', 'time'
print(route_info({'my_speed': 60}))  # Выведет: No distance info is available

