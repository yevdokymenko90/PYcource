#json
import json


'''
Для решения задачи были выполнены следующие шаги:
'''
### 1. Создание Словаря
'''
Сначала был создан словарь `data` с ключами разных типов. 
Словарь содержит разнообразные типы данных, 
включая строку (`string`), 
целое число (`integer`), 
число с плавающей точкой (`float`), 
булево значение (`boolean`), 
значение `None` (представляющее собой `null` в JSON), 
список (`list`) 
и вложенный словарь (`dict`). 
Это демонстрирует, 
как в Python можно легко работать со сложными структурами данных.
'''

data = {
    "string": "Hello, world!",
    "integer": 42,
    "float": 3.14,
    "boolean": True,
    "null": None,
    "list": [1, 2, 3],
    "dict": {"nested_string": "Hello, nested world!"}
}


### 2. Конвертация Словаря в JSON
'''
Затем, 
используя функцию `json.dumps()` 
из модуля `json`, 
словарь `data` 
был конвертирован в строку формата JSON. 
Функция `dumps()` 
принимает Python-объект 
(в данном случае словарь) 
и возвращает строку в формате JSON.
'''

json_data = json.dumps(data)


### 3. Вывод JSON и Типа Результата
'''
После конвертации были выведены на терминал 
строка JSON и тип результирующего значения. 
Вывод подтверждает, 
что результат является строкой (`str`), 
что соответствует формату JSON.
'''

print(json_data)
print(type(json_data))


### Вывод в Терминал:
'''
Результатом выполнения кода является вывод строки JSON в терминал:
'''

#{"string": "Hello, world!", "integer": 42, "float": 3.14, "boolean": true, "null": null, "list": [1, 2, 3], "dict": {"nested_string": "Hello, nested world!"}}

'''
И вывод типа результирующего значения:
'''

#<class 'str'>

'''
Это показывает, 
что словарь был успешно преобразован в строку JSON, 
что позволяет легко сериализовать структуры данных Python для хранения, 
передачи данных между системами или работы с веб-API, 
которые обычно используют JSON для обмена данными.
'''

'''
Вот цельный блок кода, 
который демонстрирует создание словаря с 
различными типами данных, 
конвертацию его в JSON и 
вывод результата вместе с типом результирующего значения. 
Код снабжен комментариями для лучшего понимания процесса.
'''

import json  # Импортирование модуля json для работы с форматом JSON

# Создание словаря с различными типами данных
data = {
    "string": "Hello, world!",  # Строковый тип
    "integer": 42,  # Целочисленный тип
    "float": 3.14,  # Число с плавающей точкой
    "boolean": True,  # Булево значение
    "null": None,  # Значение None, которое будет представлено как null в JSON
    "list": [1, 2, 3],  # Список
    "dict": {"nested_string": "Hello, nested world!"}  # Вложенный словарь
}

# Конвертация словаря в строку формата JSON
json_data = json.dumps(data)

# Вывод сконвертированной строки JSON
print("Сконвертированный словарь в JSON строку:")
print(json_data)

# Вывод типа результирующего значения
print("Тип результирующего значения:", type(json_data))


### Объяснение Кода:
'''
1. **Импорт Модуля JSON**: 
Сначала импортируется модуль `json`, 
который предоставляет функциональность для работы с JSON, 
включая сериализацию 
(конвертацию в JSON) 
и десериализацию (конвертацию из JSON) данных.

2. **Создание Словаря**: 
Создается словарь 
`data` 
с различными типами данных, 
включая строку, 
целое число, 
число с плавающей точкой, 
булево значение, 
`None`, 
список 
и другой словарь.

3. **Конвертация Словаря в JSON**:
Используя функцию 
`json.dumps()`, 
словарь 
`data` 
конвертируется в строку формата JSON. 
Функция 
`dumps()` 
преобразует Python-объекты в 
их строковое представление в формате JSON.

4. **Вывод JSON и Типа**: 
Выводится сконвертированная строка JSON и 
тип результирующего значения 
(который будет `<class 'str'>`), 
демонстрируя успешную сериализацию данных в формате JSON.

Этот код является примером того, 
как можно легко сериализовать Python-структуры данных в 
JSON для хранения, 
передачи данных между приложениями или для работы с веб-API, 
которые обычно принимают и возвращают данные в формате JSON.
'''