# # ### Создаем пустой словарь
# # user_dict = {}

# # # Трижды запрашиваем у пользователя ключ и значение
# # for i in range(3):
# #     key = input("Введите название ключа: ")
# #     value = input("Введите значение для ключа: ")
# #     user_dict[key] = value

# # # Выводим результирующий словарь
# # print(user_dict)


# # # Создаем пустой словарь
# # user_dict = {}

# # # Определяем разные запросы для каждой пары ключ-значение
# # prompts = [
# #     ("Введите название первого ключа: ", "Введите значение первого ключа: "),
# #     ("Введите название второго ключа: ", "Введите значение второго ключа: "),
# #     ("Введите название третьего ключа: ", "Введите значение третьего ключа: ")
# # ]

# # # Цикл для получения ввода от пользователя
# # for key_prompt, value_prompt in prompts:
# #     key = input(key_prompt)
# #     value = input(value_prompt)
# #     user_dict[key] = value

# # # Выводим результирующий словарь
# # print(user_dict)
# # Создаем пустой словарь
# user_dict = {}

# # Запрашиваем у пользователя данные для первой пары ключ-значение
# key1 = input("Введите название первого ключа: ")
# value1 = input("Введите значение первого ключа: ")
# user_dict[key1] = value1

# # Запрашиваем у пользователя данные для второй пары ключ-значение
# key2 = input("Введите название второго ключа: ")
# value2 = input("Введите значение второго ключа: ")
# user_dict[key2] = value2

# # Запрашиваем у пользователя данные для третьей пары ключ-значение
# key3 = input("Введите название третьего ключа: ")
# value3 = input("Введите значение третьего ключа: ")
# user_dict[key3] = value3

# # Выводим результирующий словарь
# print(user_dict)

# Создаем различные кортежи с разными типами элементов




# Кортеж с разными типами данных
example_tuple = (1, "Hello", 3.14, True)
# Кортеж с вложенными структурами (список и кортеж внутри)
nested_tuple = (1, [2, 3], (4, 5))
# Кортеж с повторяющимися элементами
repeated_tuple = ("repeat", "repeat", "repeat")

# Выводим созданные кортежи
print("Example Tuple:", example_tuple)
print("Nested Tuple:", nested_tuple)
print("Repeated Tuple:", repeated_tuple)

# Модификация кортежа
# Преобразуем кортеж example_tuple в список
my_list = list(example_tuple)

# Модифицируем список
my_list.append("new element")  # Добавляем элемент
my_list[1] = "Changed"         # Изменяем элемент
del my_list[0]                 # Удаляем первый элемент

# Преобразуем список обратно в кортеж
my_modified_tuple = tuple(my_list)

# Выводим модифицированный кортеж
print("Modified Tuple:", my_modified_tuple)



 # Создание списка с элементами разных типов
mixed_list = [42, "Hello", 3.14, [1, 2, 3], {"key": "value"}]

# Вывод списка
print(mixed_list)

# Удаление третьего элемента (элемент с индексом 2, так как индексация начинается с 0)
#del mixed_list[2]
my_list = mixed_list.pop(2)
# Вывод обновленного списка
print(len(mixed_list))
print (my_list)


# Создание списка с элементами разных типов
mixed_list = [42, "Hello", [1, 2, 3], {"key": "value"}]

# Изменение последовательности элементов в списке
mixed_list.reverse()

# Вывод обновленного списка
print(mixed_list)


second_list = ["element1", "element2"]

mixed_list.extend(second_list)

# Вывод обновленного первого списка
print(mixed_list)


# Шаг 1: Создание двух списков
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Шаг 2: Объединение двух списков с помощью оператора +
combined_list = list1 + list2

print (combined_list)

# Шаг 3: Определение магического метода, вызываемого при использовании оператора +
# Для списков это метод __add__

# Шаг 4: Выполнение слияния списков с использованием магического метода __add__
magic_method_result = list1.__add__(list2)

# Шаг 5: Вывод результатов
print("Результат слияния с помощью оператора +:", combined_list)
print("Результат слияния с помощью магического метода __add__:", magic_method_result)
