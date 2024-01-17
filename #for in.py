#for in

# Документация:
'''
Цикл for в Python используется для перебора элементов в последовательности.
Синтаксис: for <переменная> in <последовательность>:
             <блок кода>

<переменная> - это переменная, которой на каждой итерации присваивается значение из <последовательности>.
<последовательность> - это структура данных, которую мы перебираем (например, список, строка, кортеж).
<блок кода> - это код, который выполняется на каждой итерации цикла.
'''

# Пример: Перебор элементов списка и вывод их на экран
# Инициализация списка
список_чисел = [1, 2, 3, 4, 5]

# Цикл for для перебора элементов списка
for число in список_чисел:
    # Вывод каждого элемента списка
    print(число)

# В этом примере:
# 1. 'список_чисел' - это список, состоящий из чисел от 1 до 5.
# 2. Цикл for начинается с ключевого слова 'for', за которым следует переменная 'число'.
# 3. 'in список_чисел' указывает, что цикл будет перебирать элементы 'список_чисел'.
# 4. В каждой итерации цикла переменной 'число' присваивается очередное значение из списка.
# 5. 'print(число)' выводит значение переменной 'число' на каждом шаге цикла.


# Конспект:
'''
Цикл for в Python является удобным инструментом для итерации по элементам последовательности,
таким как списки, строки, словари и другие итерируемые объекты.

Синтаксис: for <переменная> in <последовательность>:
             <блок кода>
'''

# Пример 1: Перебор элементов списка и их модификация
числа = [1, 2, 3, 4, 5]
for i in range(len(числа)):
    числа[i] *= 2  # Умножаем каждое число в списке на 2
print("Удвоенные числа:", числа)

# Пример 2: Итерация по строке
строка = "Привет"
print("Символы в строке:")
for символ in строка:
    print(символ)  # Выводит каждый символ строки по отдельности

# Пример 3: Использование цикла for с словарём
словарь = {'а': 1, 'б': 2, 'в': 3}
print("Элементы словаря:")
for ключ, значение in словарь.items():
    print(f"Ключ: {ключ}, Значение: {значение}")  # Выводит ключ и значение для каждого элемента словаря

# Пример 4: Цикл for с условием break
числа = [1, 3, 4, 7, 9, 2]
print("Итерация до числа 7:")
for число in числа:
    if число == 7:
        print("Найдено число 7, останавливаем цикл.")
        break  # Выход из цикла, если встречается число 7
    print(число)

# Эти примеры демонстрируют многосторонность и гибкость цикла for в различных сценариях.


'''
Предоставленный скрипт на Python демонстрирует различные способы использования цикла `for` в разных сценариях.

**Пример 1** выполняет итерацию по списку чисел и модифицирует каждое число, умножая его на 2. 
`range(len(числа))` генерирует последовательность чисел от 0 до длины списка минус 1, 
которые используются как индексы для доступа и изменения каждого элемента списка. 
Затем модифицированный список выводится на печать.

**Пример 2** 
итерирует по строке и печатает каждый символ отдельно. 
В Python строки являются итерируемыми объектами, 
что означает возможность прохода по каждому символу строки с помощью цикла `for`.

**Пример 3** 
выполняет итерацию по словарю и печатает каждую пару ключ-значение. 
Метод `items()` используется для возврата объекта просмотра, 
который отображает список пар ключ-значение словаря в виде кортежей. 
Затем цикл `for` распаковывает каждый кортеж на `ключ` и `значение` и печатает их.

**Пример 4** 
демонстрирует использование оператора `break` в цикле `for`. 
Цикл итерирует по списку чисел и печатает каждое число до тех пор, 
пока не встретится число 7, 
после чего выводит сообщение и выходит из цикла с помощью оператора `break`. 
Оператор `break` используется для досрочного выхода из цикла, 
когда выполнено определенное условие.

Эти примеры демонстрируют универсальность и гибкость цикла `for` в Python, 
который может использоваться для итерации по различным типам итерируемых объектов 
и может управляться с помощью таких операторов, как `break`.

The provided Python script demonstrates various uses of the `for` loop in different scenarios.

**Example 1** 
iterates over a list of numbers and modifies each number by multiplying it by 2. 
The `range(len(числа))` 
generates a sequence of numbers from 0 to the length of the list minus 1, 
which are used as indices to access and modify each element of the list. 
The modified list is then printed.

**Example 2** 
iterates over a string and prints each character separately. 
In Python, strings are iterable objects, 
meaning you can loop over each character in a string using a `for` loop.

**Example 3** 
iterates over a dictionary and prints each key-value pair. 
The `items()` method 
is used to return a view object that displays 
a list of a dictionary's key-value tuple pairs. 
The `for` loop then unpacks each tuple into 
`ключ` (key) and `значение` (value) and prints them.

**Example 4** 
demonstrates the use of the `break` statement in a `for` loop. 
The loop iterates over a list of numbers and prints each number until it encounters the number 7, 
at which point it prints a message and breaks out of the loop using the `break` statement. 
The `break` statement is used to exit a loop prematurely when a certain condition is met.

These examples demonstrate the versatility and flexibility of the `for` loop in Python, 
which can be used to iterate over various types of iterable objects and 
can be controlled using statements like `break`.

'''


# Документация:
'''
В Python цикл for может использоваться для итерации по словарям. Метод items() словаря
возвращает пары ключ-значение, по которым можно итерироваться.

Синтаксис: for ключ, значение in словарь.items():
             <блок кода>

где 'ключ' и 'значение' - это переменные, которым на каждой итерации присваиваются
соответственно ключ и значение из словаря.
'''

# Пример: Итерация по словарю с использованием for и items()

# Инициализация словаря
словарь = {
    "яблоко": "зеленое",
    "банан": "желтый",
    "вишня": "красная"
}

# Итерация по словарю
for фрукт, цвет in словарь.items():
    # На каждой итерации 'фрукт' принимает значение ключа, а 'цвет' - соответствующее значение
    print(f"Фрукт: {фрукт}, Цвет: {цвет}")

# В этом примере:
# 1. Словарь 'словарь' содержит пары ключ-значение, где ключи - это названия фруктов, а значения - их цвета.
# 2. Цикл for использует метод items() для получения пар ключ-значение из словаря.
# 3. На каждой итерации переменные 'фрукт' и 'цвет' присваиваются ключу и значению текущего элемента словаря.
# 4. В блоке кода цикла происходит вывод информации о фрукте и его цвете.


# Документация:
'''
Цикл for в Python может использоваться для перебора элементов набора (множества).
Набор (множество) - это коллекция, которая содержит уникальные, неупорядоченные элементы.

Синтаксис: for <переменная> in <набор>:
             <блок кода>

где 'переменная' - это переменная, которой на каждой итерации присваивается значение элемента набора.
'''

# Инициализация набора (множества) чисел
набор_чисел = {1, 2, 3, 4, 5}

# Итерация по набору чисел
print("Элементы набора чисел:")
for число in набор_чисел:
    # На каждой итерации переменной 'число' присваивается значение одного из элементов набора
    print(число)  # Вывод каждого элемента набора

# Инициализация набора (множества) строк
набор_строк = {"яблоко", "банан", "вишня"}

# Итерация по набору строк
print("\nЭлементы набора строк:")
for фрукт in набор_строк:
    # На каждой итерации переменной 'фрукт' присваивается значение одного из элементов набора
    print(фрукт)  # Вывод каждого элемента набора

# В этих примерах:
# 1. Создаются два набора: 'набор_чисел' и 'набор_строк'.
# 2. Цикл for используется для итерации по каждому набору.
# 3. В блоке кода цикла происходит вывод каждого элемента набора.
# 4. Порядок вывода элементов может быть разным от запуска к запуску, так как наборы в Python - неупорядоченные коллекции.

# Этот пример демонстрирует, как цикл for может быть использован для эффективного перебора элементов в наборах.



# Документация:
'''
Цикл for в сочетании с функцией range используется для генерации последовательности чисел.
Функция range может принимать от одного до трех аргументов: начало диапазона, конец диапазона и шаг.

Синтаксис: for <переменная> in range(начало, конец, шаг):
             <блок кода>

где 'переменная' - это переменная, которой на каждой итерации присваивается текущее значение из диапазона.
'''

# Пример 1: Итерация по диапазону чисел от 0 до 4
print("Числа от 0 до 4:")
for i in range(5):
    # range(5) генерирует последовательность чисел от 0 до 4 (5 не включается)
    print(i)  # Вывод текущего числа

# Пример 2: Итерация по диапазону с определенным шагом
print("\nЧисла от 1 до 10 с шагом 2:")
for i in range(1, 11, 2):
    # range(1, 11, 2) генерирует числа от 1 до 10 с шагом 2
    print(i)  # Вывод текущего числа

# Пример 3: Обратный отсчет
print("\nОбратный отсчет от 5 до 1:")
for i in range(5, 0, -1):
    # range(5, 0, -1) генерирует обратную последовательность от 5 до 1
    print(i)  # Вывод текущего числа

# В этих примерах:
# 1. Используется функция range для создания последовательности чисел.
# 2. Цикл for используется для итерации по этим последовательностям.
# 3. В первом примере range(5) создает последовательность от 0 до 4.
# 4. Во втором примере range(1, 11, 2) создает последовательность от 1 до 10 с шагом 2.
# 5. В третьем примере range(5, 0, -1) создает обратную последовательность от 5 до 1.
# 6. На каждой итерации цикла переменной 'i' присваивается текущее значение из диапазона.
# 7. В блоке кода цикла происходит вывод текущего значения переменной 'i'.
# Эти примеры демонстрируют, как можно использовать функцию range с разными параметрами для управления потоком итераций в цикле for.

