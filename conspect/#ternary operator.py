#ternary operator

my_number = 21.5

print("is int") if type(my_number) is int else print("is not int")


# Документация:
'''
Тернарный оператор используется для определения значения переменной на основе логического условия.
Синтаксис: переменная = значение1 if условие else значение2
'''

# Пример:
# Предположим, нам нужно определить, является ли число положительным, отрицательным или равным нулю.

число = 5

# Использование тернарного оператора для определения результата
результат = "Положительное" if число > 0 else "Отрицательное" if число < 0 else "Ноль"

print(результат)  # Вывод: Положительное

# В этом примере:
# 1. Если 'число' больше нуля, 'результат' становится "Положительное".
# 2. Если 'число' меньше нуля, 'результат' становится "Отрицательное".
# 3. Если 'число' равно нулю, 'результат' становится "Ноль".




# Документация:
'''
Тернарный оператор в Python используется для сокращенной записи условных выражений.
Его синтаксис: <значение_если_истина> if <условие> else <значение_если_ложь>

Этот оператор удобен для простых условных присваиваний. Однако для сложных условий
лучше использовать полную форму if-else для лучшей читаемости кода.
'''

# Пример использования тернарного оператора для определения типа числа

# Входное число
число = -4

# Использование тернарного оператора для определения типа числа
# Шаг 1: Проверяем, положительное ли число
# Шаг 2: Если условие истинно (число > 0), присваиваем результату строку "Положительное"
# Шаг 3: Если условие ложно (число <= 0), проверяем, является ли число отрицательным
# Шаг 4: Если число отрицательное (число < 0), присваиваем результату строку "Отрицательное"
# Шаг 5: Если число равно 0, присваиваем результату строку "Ноль"



product_qty = 10

print("In stock") if product_qty > 0 else print("Out of stock")


'''
The provided Python script defines a variable `product_qty` 
and assigns it the integer value `10`. 
It then uses a ternary (conditional) operator 
to check if `product_qty` is greater than `0`.

A ternary operator is a shorter way to write an `if-else` statement and works like this: 
`value_if_true if condition else value_if_false`. 
In this case, if `product_qty` is greater than `0`, 
it prints "In stock". 
If `product_qty` is not greater than `0`, it prints "Out of stock".

The `print()` function is a built-in Python function used to output text to the console. 
It takes multiple arguments and prints them to the console. 
In this script, it's used to print either "In stock" or "Out of stock" 
based on the value of `product_qty`.

In this case, since `product_qty` is `10` which is greater than `0`, 
the output of this script will be "In stock". 
If `product_qty` was `0` or less, the output would be "Out of stock".

The function implementations you provided are the built-in Python `print()` function. 
It takes several parameters: `values` which are the objects to be printed, 
`sep` which is the separator between the `values` (default is a space), 
`end` which is the character to be printed at the end (default is a newline), 
`file` which is the file where the values are printed 
(default is `None`, meaning values are printed to the console), 
and `flush` which determines whether the output is flushed (default is `False`).
'''

my_img = ('1920', '1080')

print(f"{my_img[0]}x{my_img[1]}") if len(my_img) == 2 else print("Incorrect format")


'''
The provided Python script defines a tuple 
`my_img` with two elements: '1920' and '1080'. 
These elements represent the width and height of an image in pixels.

The script then uses a ternary (conditional) operator 
to check if the length of `my_img` is exactly 2. 
The `len()` function is a built-in Python function that returns the number of items in an object. 
In this case, it's used to count the number of elements in the `my_img` tuple.

The ternary operator works like this: 
`value_if_true if condition else value_if_false`. 
If the length of `my_img` is exactly 2, 
it prints a formatted string with the width and height of the image. 
The `f-string` (formatted string literal) is a way to embed expressions inside string literals, 
using curly braces `{}`. 
The expressions will be replaced with their values when the string is printed.

If the length of `my_img` is not 2, 
it prints "Incorrect format". 
This could be the case if the tuple has more or fewer than two elements, 
which would not correctly represent an image's dimensions.

The `print()` function is a built-in Python function used to output text to the console. 
In this script, it's used to print either the image dimensions 
or "Incorrect format" based on the length of `my_img`.

In this case, since `my_img` has exactly two elements, 
the output of this script will be "1920x1080". 
If `my_img` had more or fewer than two elements, the output would be "Incorrect format".
'''

my_img = ('1920', '1080')

info = f"{my_img[0]}x{my_img[1]}" if len(my_img) == 2 else print("Incorrect format")

print(info)



# Цель данного блока кода - проверить, соответствует ли формат данных в кортеже 'my_img'
# ожидаемому (две записи, представляющие размеры изображения) и в зависимости от этого
# формировать строку с информацией о размерах изображения или выводить сообщение об ошибке.

# Шаг 1: Инициализация кортежа 'my_img'
my_img = ('1920', '1080')  # Кортеж, содержащий ширину и высоту изображения в пикселях.

# Шаг 2: Проверка условия с использованием конструкции if-else
if len(my_img) == 2:
    # Шаг 2.1: Если в кортеже ровно два элемента, форматируем строку с размерами
    info = f"{my_img[0]}x{my_img[1]}"  # Формирование строки с использованием f-string для вставки значений.
else:
    # Шаг 2.2: Если в кортеже не два элемента, выводим сообщение об ошибке
    print("Incorrect format")  # Вывод сообщения об ошибке
    info = None  # Присваиваем 'info' значение None, так как формат данных некорректен.

# Шаг 3: Вывод результата
print(info)  # Вывод значения переменной 'info'. Будет либо строка с размерами, либо None.

# Этот блок кода иллюстрирует использование условных операторов для проверки корректности
# данных и соответствующего формирования вывода программы.
