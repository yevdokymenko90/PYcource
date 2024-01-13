"""
    Merge two lists into a dictionary.

    Args:
        list_one (list): The first list.
        list_two (list): The second list.

    Returns:
        dict: A dictionary where the elements of list_one are the keys and the elements of list_two are the values.
    """


def merge_lists_to_dict(list_one, list_two):

    zipped_seq = zip(list_one, list_two)
    return dict(zipped_seq)


def merge_lists_to_dict_alternative(list_one, list_two):
    return dict(zip(list_one, list_two))


'''
Ваш код содержит две функции: 
`merge_lists_to_dict` и `merge_lists_to_dict_alternative`. 
Обе функции принимают два списка в качестве аргументов и возвращают словарь, 
где элементы первого списка являются ключами, 
а элементы второго списка - значениями.

Первая функция, `merge_lists_to_dict`, 
использует функцию `zip` для создания итератора кортежей, 
где каждый кортеж содержит соответствующие элементы из каждого списка. 
Затем этот итератор передается функции `dict`, 
которая преобразует его в словарь.

Вторая функция, `merge_lists_to_dict_alternative`, делает то же самое, 
но в более компактной форме. 
Она объединяет вызовы `zip` и `dict` в одной строке, 
возвращая результат непосредственно.

Обе функции предполагают, что оба списка имеют одинаковую длину. 
Если списки разной длины, `zip` прекратит объединение, 
как только достигнет конца самого короткого списка, 
и оставшиеся элементы длинного списка будут игнорироваться. 
Если вам нужно обработать списки разной длины, вам нужно будет изменить подход.
'''

# Example 1:
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
result = merge_lists_to_dict(list1, list2)
print(result)
# Output: {1: 'a', 2: 'b', 3: 'c'}

# Example 2:
list1 = ['apple', 'banana', 'cherry']
list2 = [1.0, 2.0, 3.0]
result = merge_lists_to_dict(list1, list2)
print(result)
# Output: {'apple': 1.0, 'banana': 2.0, 'cherry': 3.0}

# Example 3:
list1 = ['red', 'green', 'blue']
list2 = [True, False, True]
result = merge_lists_to_dict(list1, list2)
print(result)
# Output: {'red': True, 'green': False, 'blue': True}


# В представленном коде определена функция `merge_lists_to_dict(list_one, list_two)`, 
# которая принимает два списка в качестве аргументов. Эта функция объединяет два списка в словарь, 
# где элементы из первого списка становятся ключами, а элементы из второго списка - значениями.

# Для этого используется функция `zip(list_one, list_two)`, 
# которая возвращает итератор кортежей, 
# где первый элемент в каждом кортеже берется из первого списка, 
# а второй - из второго. 
# Это позволяет сопоставить каждому элементу из первого списка элемент из второго списка.

# Затем полученный итератор кортежей преобразуется в словарь с помощью функции `dict()`. 
# В результате получается словарь, где ключи - это элементы из первого списка, а значения - из второго.

# В коде также приведены три примера использования этой функции с различными типами данных. 
# В первом примере списки содержат целые числа и строки, во втором - строки и вещественные числа, 
# а в третьем - строки и булевы значения. В каждом случае функция успешно создает словарь из двух списков.



# Определение функции с ключевыми аргументами.
# Символ '*' требует, чтобы аргументы передавались с использованием их имен (ключевые аргументы).
def merge_lists_to_dict_alternative(*, list_one, list_two):
    """
    Объединяет два списка в словарь.

    Функция принимает два списка, `list_one` и `list_two`, и объединяет их в словарь.
    Каждый элемент из `list_one` становится ключом, а соответствующий элемент из `list_two` - значением.

    Аргументы:
    list_one (list): Список ключей.
    list_two (list): Список значений.

    Возвращает:
    dict: Словарь, сформированный путем соединения `list_one` и `list_two`.
    """
    return dict(zip(list_one, list_two))

def zip_lists_to_dict(list_one, *, list_two):
    """
    Объединяет два списка в словарь.

    Функция принимает один позиционный аргумент `list_one` и один ключевой аргумент `list_two`.
    Каждый элемент из `list_one` становится ключом, а соответствующий элемент из `list_two` - значением.

    Аргументы:
    list_one (list): Список ключей.
    list_two (list): Список значений.

    Возвращает:
    dict: Словарь, сформированный путем соединения `list_one` и `list_two`.
    """
    return dict(zip(list_one, list_two))

# Пример использования merge_lists_to_dict_alternative
example_list_one_alt = [1, 2, 3]
example_list_two_alt = ['a', 'b', 'c']
result_alt = merge_lists_to_dict_alternative(list_one=example_list_one_alt, list_two=example_list_two_alt)
print(result_alt)  # Вывод: {1: 'a', 2: 'b', 3: 'c'}

# Пример использования zip_lists_to_dict
example_list_one_zip = [4, 5, 6]
example_list_two_zip = ['d', 'e', 'f']
result_zip = zip_lists_to_dict(example_list_one_zip, list_two=example_list_two_zip)
print(result_zip)  # Вывод: {4: 'd', 5: 'e', 6: 'f'}




def update_car_info(brand=None, price=None):
    """
    Обновляет информацию о машине, создавая словарь с заданными параметрами,
    добавляет ключ 'is_available' со значением True и возвращает измененный словарь.

    Параметры:
    brand (str): Марка машины.
    price (int): Цена машины.

    Возвращает:
    dict: Словарь с обновленной информацией о машине.
    """
    car = {'brand': brand, 'price': price}
    car['is_available'] = True
    return car

# Вызов функции с именованными аргументами
updated_car_info = update_car_info(brand="Toyota", price=20000)

# Вывод результата
print(updated_car_info)  # Вывод: {'brand': 'Toyota', 'price': 20000, 'is_available': True}


'''
В этом коде:

Функция update_car_info определена с двумя именованными параметрами brand и price. 
Каждый из них имеет значение по умолчанию None, 
что позволяет вызвать функцию без обязательного указания всех параметров.
В теле функции создается словарь car с этими параметрами.
Добавляется ключ is_available со значением True.
Функция возвращает словарь car.
В вызове функции можно указывать значения brand и price, 
и результат будет выведен на экран.
'''



def update_car_info(**kwargs):
    """
    Обновляет информацию о машине, объединяя все именованные аргументы в словарь,
    добавляет ключ 'is_available' со значением True и возвращает измененный словарь.

    **kwargs: Именованные аргументы, содержащие информацию о машине.
    
    Возвращает:
    dict: Словарь с обновленной информацией о машине.
    """
    car = kwargs  # Объединение именованных аргументов в словарь
    car['is_available'] = True  # Добавление нового ключа
    return car

# Вызов функции с именованными аргументами
updated_car_info = update_car_info(brand="Toyota", price=20000)

# Вывод результата
print(updated_car_info)  # Вывод: {'brand': 'Toyota', 'price': 20000, 'is_available': True}
'''
В этом коде:

Функция update_car_info принимает произвольное количество именованных аргументов (**kwargs), 
которые автоматически объединяются в словарь car.
Затем в словарь добавляется ключ is_available со значением True.
В конце функция возвращает измененный словарь car.
Функция вызывается с именованными аргументами brand и price, 
значения которых могут быть любыми, и результат выводится на экран.
'''


'''
Вы создали функцию updated_car_info, 
которая принимает произвольное количество именованных аргументов, 
собирая их в словарь car благодаря использованию **car. 
Затем вы добавляете в этот словарь ключ is_available 
со значением True и возвращаете измененный словарь.

Однако в вашем примере вызывается функция update_car_info, 
которая, судя по всему, должна быть updated_car_info. 
Вот исправленный вариант вашего кода:
'''
def updated_car_info(**car):
    car['is_available'] = True
    return car

res = update_car_info(brand="Toyota", price=20000)
print(res)  # Вывод: {'brand': 'Toyota', 'price': 20000, 'is_available': True}



'''
'''
