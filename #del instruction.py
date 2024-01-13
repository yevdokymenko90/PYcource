#del instruction

my_dict = {'a': True, 'b': 26}

del my_dict['a']

my_dict.__delitem__('b')

print(my_dict)

print(my_dict.__delitem__)

'''
Активный выбор - это Python скрипт, 
который демонстрирует, 
как удалять элементы из словаря с помощью инструкции `del` и метода `__delitem__`.

В Python словарь - это коллекция пар ключ-значение. 
Он определяется путем заключения пар ключ-значение, 
разделенных запятыми, в фигурные скобки `{}`. 
Каждый ключ отделяется от своего значения двоеточием `:`.

В первой части кода создается словарь с именем 
`my_dict` с парами ключ-значение `'a': True` и `'b': 26`.

Затем используется инструкция `del` 
для удаления элемента с ключом `'a'` из `my_dict`. 
Инструкция `del` в Python - это способ удалить объекты. 
В данном случае она используется для удаления пары ключ-значение из словаря. 
После выполнения этой строки кода в `my_dict` будет содержаться только пара ключ-значение `'b': 26`.

Затем используется метод `__delitem__` 
для удаления элемента с ключом `'b'` из `my_dict`. 
Метод `__delitem__` - это специальный метод в Python, 
который используется для удаления элемента в контейнере. 
Он эквивалентен инструкции `del`, но используется в форме метода. 
После выполнения этой строки кода `my_dict` будет пустым словарем.

Наконец, функция `print` используется для вывода `my_dict` и `my_dict.__delitem__` в консоль.
Функция `print` в Python отправляет данные на стандартное устройство вывода (экран или оболочку). 
В данном случае она будет выводить содержимое `my_dict` и метод `__delitem__` объекта `my_dict`.

Вывод этого скрипта будет:

```python
{}
<method-wrapper '__delitem__' of dict object at 0x7f8c4830c820>
```

Это показывает, что `my_dict` - это пустой словарь 
после выполнения инструкции `del` и метода `__delitem__`, 
а `my_dict.__delitem__` - это объект method-wrapper.
'''

my_list = [1,2]

del my_list[0]

my_list.__delitem__(0)

print(my_list) 

'''
Активный выбор - это Python скрипт, который демонстрирует, 
как удалять элементы из списка с помощью инструкции `del` и метода `__delitem__`.

В Python список - это коллекция элементов, 
которые упорядочены и изменяемы. 
Он определяется путем заключения списка элементов, 
разделенных запятыми, в квадратные скобки `[]`.

В первой части кода создается список с именем 
`my_list` с элементами `1` и `2`.

Затем используется инструкция `del` 
для удаления элемента с индексом `0` из `my_list`. 
Инструкция `del` в Python - это способ удалить объекты. 
В данном случае она используется для удаления элемента из списка по его индексу. 
После выполнения этой строки кода в `my_list` будет содержаться только элемент `2`.

Затем используется метод `__delitem__` 
для удаления элемента с индексом `0` из `my_list`. 
Метод `__delitem__` - это специальный метод в Python, 
который используется для удаления элемента в контейнере. 
Он эквивалентен инструкции `del`, но используется в форме метода. 
После выполнения этой строки кода `my_list` будет пустым списком.

Наконец, функция `print` используется для вывода `my_list` в консоль. 
Функция `print` в Python отправляет данные на стандартное устройство вывода (экран или оболочку). 
В данном случае она будет выводить содержимое `my_list`.

Вывод этого скрипта будет:

```python
[]
```

Это показывает, 
что `my_list` - это пустой список после выполнения инструкции `del` и метода `__delitem__`.
'''

