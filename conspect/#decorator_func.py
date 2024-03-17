#decorator_func

'''
Функция-декоратор в Python — это функция, 
которая позволяет изменить или расширить поведение других функций или методов 
без их прямого изменения. 
Декораторы обертывают другую функцию и 
могут выполнять некоторые операции до или после 
основной функции. 
Они предоставляют гибкий способ добавления функциональности, 
что улучшает читаемость и поддерживаемость кода.

В Python декораторы часто используются для логирования, 
проверки доступа, 
измерения времени выполнения функций и многих других задач.

Давайте рассмотрим пример простого декоратора:
'''
### Пример: Декоратор для Логирования


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Вызывается функция: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} завершила выполнение")
        return result
    return wrapper

@log_decorator
def greet(name):
    print(f"Привет, {name}!")

greet("Алиса")

'''

В этом примере:

1. **Определение Декоратора**: 
`log_decorator` — это функция-декоратор, 
которая принимает функцию `func` в качестве аргумента.

2. **Функция-обертка `wrapper`**: 
Внутри `log_decorator` определена вложенная функция `wrapper`, 
которая оборачивает вызов `func`. 
Она позволяет выполнить дополнительные действия до 
и после вызова `func`.

3. **Применение Декоратора**: 
Декоратор `@log_decorator` применяется к функции `greet`. 
Это означает, что когда `greet` вызывается, 
вызов проходит через `wrapper`.

4. **Вызов функции `greet`**: 
При вызове `greet`, 
сначала выводится сообщение о начале вызова функции, 
затем выполняется основное тело функции `greet`, 
и после её выполнения выводится сообщение о завершении.

Декораторы являются мощным инструментом в Python, 
позволяя эффективно модифицировать поведение функций и методов.
'''


'''
более подробно разберем концепцию функций-декораторов в Python, 
используя простой пример.

### Что такое Декоратор?

Функция-декоратор в Python — это функция, 
которая принимает другую функцию в качестве аргумента, 
добавляет к ней некоторую функциональность и 
возвращает новую функцию. 
С помощью декораторов можно 
легко модифицировать поведение существующих функций 
без изменения их кода.

### Пример Декоратора

Допустим, у нас есть декоратор, который логирует начало и конец выполнения функции.

#### 1. Определение Декоратора
'''


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Начало выполнения функции: {func.__name__}")
        result = func(*args, **kwargs)  # Вызов оригинальной функции
        print(f"Конец выполнения функции: {func.__name__}")
        return result
    return wrapper

'''
Здесь `log_decorator` — это функция-декоратор. 
Она принимает функцию `func` и 
возвращает новую функцию `wrapper`. 
`wrapper` — это обертка вокруг оригинальной функции `func`, 
добавляющая дополнительные действия перед и после вызова `func`.

#### 2. Применение Декоратора

'''


@log_decorator
def greet(name):
    print(f"Привет, {name}!")

'''
С помощью символа `@` мы применяем декоратор `log_decorator` к функции `greet`. Это эквивалентно записи `greet = log_decorator(greet)`.

#### 3. Вызов Декорированной Функции
'''

greet("Мир")

'''
При вызове `greet("Мир")`, 
сначала выполняется код внутри `wrapper` из `log_decorator`, 
который логирует начало выполнения, 
затем вызывает оригинальную функцию `greet`, 
и после ее выполнения логирует конец выполнения.

### Вывод

Декораторы предоставляют элегантный способ изменения поведения функций, 
что особенно полезно для логирования, 
измерения производительности, 
проверки предусловий и других общих задач в программировании.
'''



'''
В автоматизированном тестировании с использованием Playwright, 
декораторы в Python могут быть использованы для 
расширения и улучшения функциональности тестов, 
не изменяя их основной логики. 
Декораторы могут применяться для различных целей, 
включая логирование, 
подготовку и очистку тестовых данных, 
параметризацию тестов, 
обработку исключений и многое другое.

Давайте рассмотрим несколько примеров того, 
как декораторы могут быть полезны 
в контексте автоматизированного тестирования с Playwright.



### 1. Логирование

Декоратор для логирования может использоваться для 
записи информации 
о начале и 
окончании выполнения тестов, 
что помогает в отладке и мониторинге.

Представленный Python скрипт демонстрирует 
использование декораторов для логирования начала 
и конца выполнения функции, 
что может быть полезно для отладки и 
тестирования производительности.

Скрипт определяет функцию-декоратор 
`log_test`. 
Эта функция принимает другую функцию 
`func` 
в качестве аргумента и 
определяет внутри себя функцию-обертку 
`wrapper`. 
Эта структура типична для декораторов Python, 
которые используются для изменения поведения функции или класса.

Внутри функции 
`wrapper` 
сначала выводится сообщение, 
указывающее на начало выполнения функции. 
Сообщение включает имя функции, 
которое получается с помощью 
`func.__name__`. 
Затем вызывается исходная функция 
`func` 
с любыми аргументами и 
ключевыми аргументами, 
которые были переданы в 
`wrapper`. 

После вызова функции выводится другое сообщение, 
указывающее на окончание выполнения функции. 
Это означает, 
что когда функция декорируется с помощью 
`@log_test`, 
она сначала логирует начало своего выполнения, 
затем выполняет исходную функцию, 
и, наконец, 
логирует окончание своего выполнения.

Функция-декоратор 
`log_test` 
затем используется для декорирования функции 
`test_example`. 
Это означает, 
что всякий раз, 
когда вызывается 
`test_example`, 
сначала логируется начало его выполнения, 
затем выполняется его собственная логика, и, наконец, 
логируется окончание его выполнения. 
В данном случае у 
`test_example` 
нет собственной логики; 
это просто заглушка для демонстрации работы декоратора.

Функция `print` - это встроенная функция Python, 
которая выводит текст в консоль. 
В данном случае она используется для 
вывода сообщений, 
указывающих на начало и 
конец выполнения функции. 
Реализации функции, 
которые вы предоставили, 
являются стандартной функцией `print()` Python, 
которая принимает любое количество аргументов и 
печатает их, 
разделенные 
`sep` 
и следующие за 
`end`. 
`file` и `flush` - это необязательные аргументы, 
которые указывают, 
где печатать и следует ли очищать буфер вывода.

'''

def log_test(func):
    """
    A decorator function that logs the start and 
    end of the decorated function's execution.

    Args:
        func: The function to be decorated.

    Returns:
        The wrapper function that logs the start and 
        end of the decorated function's execution.
    """
    def wrapper(*args, **kwargs):
        print(f"Тест {func.__name__} начал выполнение")
        result = func(*args, **kwargs)
        print(f"Тест {func.__name__} завершил выполнение")
        return result
    return wrapper

@log_test
def test_example():
    # Логика теста
    pass


'''
The provided Python script 
demonstrates the use of decorators 
for logging the start and end of a function's execution, 
which can be useful for debugging and performance testing.

The script defines a decorator function `log_test`. 
This function takes another function `func` 
as an argument and defines a wrapper function `wrapper` inside it. 
This structure is typical for Python decorators, 
which are a way to modify the behavior of a function or class.

Inside the `wrapper` function, 
it first prints a message indicating the start of the function's execution. 
The message includes the name of the function, 
which is accessed using `func.__name__`. 
Then, it calls the original function `func` 
with any arguments and keyword arguments that were passed to `wrapper`. 
After the function call, 
it prints another message indicating the end of the function's execution. 
This means that when a function is decorated with `@log_test`, 
it will first log the start of its execution, 
then execute the original function, 
and finally log the end of its execution.

The decorator function 
`log_test` 
is then used to decorate the function 
`test_example`. 
This means that whenever 
`test_example` 
is called, 
it will first log the start of its execution, 
then execute its own logic, 
and finally log the end of its execution. 
In this case, 
`test_example` 
doesn't have any logic of its own; 
it's just a placeholder 
to demonstrate how the decorator works.

The `print` function is a built-in Python function that outputs text to the console. 
In this case, it's used to print messages indicating the start and end of the function's execution. 
The function implementations you provided are 
the standard Python `print()` function, 
which takes any number of arguments and prints them, 
separated by 
`sep` 
and followed by 
`end`. 
`file` and `flush` 
are optional arguments that 
specify where to print and whether to flush 
the output buffer, respectively.
'''


'''
### 2. Подготовка и Очистка Тестовых Данных
Декораторы могут использоваться для выполнения подготовительных и завершающих действий 
(например, настройки тестовых данных или их очистки после теста).

The provided Python script demonstrates the use of decorators 
for setup and teardown operations, 
which are common in testing scenarios. 

The script defines a decorator function `setup_and_teardown`. 
This function takes another function `func` 
as an argument and defines a wrapper function `wrapper` inside it. 
This structure is typical for Python decorators, 
which are a way to modify the behavior of a function or class.

Inside the `wrapper` function, 
it first prints a message "Настройка тестовых данных" 
(which translates to "Setting up test data") 
to simulate setup operations. 
Then, it calls the original function `func` 
with any arguments and keyword arguments that were passed to `wrapper`. 
After the function call, 
it prints another message "Очистка тестовых данных" 
(which translates to "Cleaning up test data") 
to simulate teardown operations. 
This means that when a function is decorated with `@setup_and_teardown`, 
it will first perform the setup operations, 
then execute the original function, 
and finally perform the teardown operations.

The decorator function `setup_and_teardown` 
is then used to decorate the function `test_example`. 
This means that whenever `test_example` is called, 
it will first execute the setup operations, 
then execute its own logic, 
and finally execute the teardown operations. 
In this case, 
`test_example` 
doesn't have any logic of its own; 
it's just a placeholder to demonstrate how the decorator works.

The `print` function is a built-in Python function that outputs text to the console. 
In this case, 
it's used to print messages indicating the setup and teardown operations. 
The function implementations you provided are the standard Python `print()` function, 
which takes any number of arguments and prints them, separated by `sep` and followed by `end`. 
`file` and `flush` are optional arguments that specify where to print and whether to flush the output buffer, respectively.

'''

def setup_and_teardown(func):
    """
    Decorator function that performs setup and teardown operations before and 
    after the decorated function is called.

    Args:
        func: The function to be decorated.

    Returns:
        The decorated function.
    """
    def wrapper(*args, **kwargs):
        # Подготовка перед тестом
        print("Настройка тестовых данных")
        result = func(*args, **kwargs)
        # Очистка после теста
        print("Очистка тестовых данных")
        return result
    return wrapper

@setup_and_teardown
def test_example():
    # Логика теста
    pass

'''

Данный Python скрипт демонстрирует использование декораторов для 
выполнения операций подготовки и завершения, 
которые часто используются в сценариях тестирования.

Скрипт определяет функцию-декоратор 
`setup_and_teardown`. 

Эта функция принимает другую функцию 
`func` 
в качестве аргумента и определяет внутри себя функцию-обертку 
`wrapper`. 
Эта структура типична для декораторов Python, 
которые используются для изменения поведения функции или класса.

Внутри функции 
`wrapper` 
сначала выводится сообщение "Настройка тестовых данных" 
для имитации операций подготовки. 
Затем вызывается исходная функция 
`func` 
с любыми аргументами и ключевыми аргументами, 
которые были переданы в `wrapper`.
 
После вызова функции выводится другое сообщение "Очистка тестовых данных" 
для имитации операций завершения. 
Это означает, 
что когда функция декорируется с помощью 
`@setup_and_teardown`, 
сначала выполняются операции подготовки, 
затем выполняется исходная функция, 
и, наконец, выполняются операции завершения.

Функция-декоратор `setup_and_teardown` 
затем используется для декорирования функции 
`test_example`. 
Это означает, что всякий раз, 
когда вызывается 
`test_example`, 
сначала выполняются операции подготовки, 
затем выполняется собственная логика, и, наконец, 
выполняются операции завершения. 
В данном случае у 
`test_example` 
нет собственной логики; 
это просто заглушка для демонстрации работы декоратора.

'''




'''
### 3. Повторное Использование Кода

Декораторы могут быть использованы для устранения дублирования кода, 
путем вынесения общей логики в декораторы.

The provided Python script demonstrates 
the use of decorators to avoid code duplication 
by extracting common logic into decorators.

The script starts by defining a decorator function 
`with_authenticated_user`. 
This function takes another function `func` as an argument 
and defines a wrapper function `wrapper` 
inside it. 
This structure is typical for Python decorators, 
which are a way to modify the behavior of a function or class.

Inside the `wrapper` function, 
it prints a message "Аутентификация пользователя" (which translates to "User authentication") 
to simulate user authentication logic. 
After this, it calls the original function `func` 
with any arguments and keyword arguments that were passed to `wrapper`. 
This means that when a function is decorated with `@with_authenticated_user`, 
it will first print the message and then execute the original function.

The decorator function `with_authenticated_user` 
is then used to decorate the function `test_example`. 
This means that whenever `test_example` is called, 
it will first execute the user authentication logic (printing the message) 
and then execute its own logic. 
In this case, `test_example` doesn't have any logic of its own; 
it's just a placeholder to demonstrate how the decorator works.

The `print` function is a built-in Python function 
that outputs text to the console. 
In this case, 
it's used to print a message indicating that 
user authentication is taking place. 
The function implementations you provided are 
the standard Python `print()` function, 
which takes any number of arguments and prints them, 
separated by `sep` and followed by `end`. 
`file` and `flush` are optional arguments 
that specify where to print and whether to flush the output buffer, 
respectively.
'''


def with_authenticated_user(func):
    """
    Decorator function that performs user authentication before executing the decorated function.

    Args:
        func: The function to be decorated.

    Returns:
        The decorated function.
    """
    def wrapper(*args, **kwargs):
        # Логика для аутентификации пользователя
        print("Аутентификация пользователя")
        return func(*args, **kwargs)
    return wrapper

@with_authenticated_user
def test_example():
    # Логика теста, требующего аутентификации
    pass


'''
Данный Python скрипт демонстрирует использование декораторов для 
избежания дублирования кода 
путем вынесения общей логики в декораторы.

Скрипт начинает с определения функции-декоратора 
`with_authenticated_user`. 
Эта функция принимает другую функцию `func` 
в качестве аргумента 
и определяет внутри себя функцию-обертку `wrapper`. 

Эта структура типична для декораторов Python, 
которые используются для изменения поведения функции или класса.

Внутри функции `wrapper` 
выводится сообщение "Аутентификация пользователя" 
для имитации логики аутентификации пользователя. 
После этого вызывается исходная функция `func` 
с любыми аргументами и ключевыми аргументами, 
которые были переданы в `wrapper`. 
Это означает, что 
когда функция декорируется с помощью 
`@with_authenticated_user`, 
сначала выводится сообщение, 
а затем выполняется исходная функция.

Функция-декоратор `with_authenticated_user` 
затем используется для декорирования функции `test_example`.
Это означает, 
что всякий раз, 
когда вызывается `test_example`, 
сначала выполняется логика аутентификации пользователя (вывод сообщения), 
а затем выполняется собственная логика. 
В данном случае у `test_example` нет собственной логики; 
это просто заглушка для демонстрации работы декоратора.

'''




'''
### 4. Параметризация Тестов

Декораторы могут использоваться для параметризации тестов, 
позволяя запускать один и тот же тест с разными наборами данных.

The provided Python script defines 
a parameterized decorator and 
uses it to modify the behavior of a function.

The script starts by defining a function 
`parameterized` 
that takes any number of arguments (`*args`). 
This function defines and returns another function `decorator`, 
which takes a single argument `func`. 
This structure is typical for Python decorators, 
which are a way to modify the behavior of a function or class.

Inside the `decorator` function, 
a `for` loop iterates over the arguments passed to `parameterized`. 
For each argument, it prints a message and then calls `func` with the argument. 
This means that when a function is decorated with `@parameterized`, 
it will be called once for each argument passed to `parameterized`, 
and a message will be printed before each call.

The `print` function is a built-in Python function that outputs text to the console. 
In this case, it's used to print a message indicating the current argument.

The script then defines a function `test_example` 
and decorates it with `@parameterized(1, 2, 3)`. 
This means that `test_example` will be passed to the `decorator` 
function as `func`, and `1`, `2`, and `3` will be passed as arguments to `parameterized`. 
As a result, `test_example` will be called three times: 
once with `1`, 
once with `2`, 
and once with `3`, 
and a message will be printed before each call.

The `test_example` function itself doesn't do anything in this script; 
it's just a placeholder to demonstrate how the decorator works. 
In a real-world application, 
it would contain some logic that uses the argument `arg`.

'''

def parameterized(*args):
    """
    A decorator factory that takes in arguments and returns a decorator.

    Args:
        *args: Variable number of arguments.

    Returns:
        decorator: A decorator function.

    """
    def decorator(func):
        for arg in args:
            print(f"Тест с аргументом: {arg}")
            func(arg)
    return decorator

@parameterized(1, 2, 3)
def test_example(arg):
    # Логика теста с использованием аргумента arg
    pass

'''
Данный Python скрипт определяет параметризованный декоратор и использует его для изменения поведения функции.

Скрипт начинает с определения функции `parameterized`, 
которая принимает любое количество аргументов (`*args`). 
Эта функция определяет и возвращает другую функцию `decorator`, 
которая принимает один аргумент `func`. 

Такая структура типична для декораторов Python, 
которые используются для изменения поведения функции или класса.

Внутри функции `decorator` цикл `for` проходит по аргументам, 
переданным в `parameterized`. 
Для каждого аргумента он выводит сообщение, 
а затем вызывает `func` с этим аргументом. 
Это означает, что когда функция декорируется с помощью `@parameterized`, 
она будет вызвана один раз для каждого аргумента, 
переданного в `parameterized`, 
и перед каждым вызовом будет напечатано сообщение.

Функция `print` - это встроенная функция Python, 
которая выводит текст в консоль. 
В данном случае она используется для вывода сообщения, 
указывающего текущий аргумент.

Затем скрипт определяет функцию `test_example` 
и декорирует ее с помощью `@parameterized(1, 2, 3)`. 
Это означает, что `test_example` будет передана в функцию `decorator` в качестве `func`, 
а `1`, `2` и `3` 
будут переданы в качестве аргументов в `parameterized`. 
В результате `test_example` 
будет вызвана три раза: 
один раз с `1`, 
один раз с `2` 
и один раз с `3`, 
и перед каждым вызовом будет напечатано сообщение.

Сама функция `test_example` 
в этом скрипте ничего не делает; 
она просто служит заглушкой для демонстрации работы декоратора. 
В реальном приложении она содержала бы некую логику, 
использующую аргумент `arg`.


Эти примеры демонстрируют, 
как декораторы могут улучшить структуру и 
организацию автоматизированных тестов в Playwright, 
делая их более гибкими, 
удобочитаемыми и легко поддерживаемыми.
'''


