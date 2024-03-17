'''
from selenium import webdriver
import pytest

# Функция для входа в систему, которая принимает веб-драйвер и колбек-функцию
def login_to_site(browser, after_login_callback=None):
    """
    Функция выполняет вход на сайт и, если предоставлена, вызывает колбек-функцию.

    :param browser: экземпляр веб-драйвера
    :param after_login_callback: функция обратного вызова, которая выполнится после входа
    """
    # Процесс входа в систему
    browser.get("https://example.com/login")
    username_field = browser.find_element_by_id("username")
    password_field = browser.find_element_by_id("password")
    
    username_field.send_keys("user")
    password_field.send_keys("password")
    login_button = browser.find_element_by_id("login_button")
    login_button.click()

    # Проверка успешного входа в систему
    assert browser.find_element_by_id("welcome_message")

    # Если предоставлена колбек-функция, вызвать её
    if after_login_callback:
        after_login_callback(browser)

# Фикстура pytest для создания и закрытия веб-драйвера
@pytest.fixture
def browser():
    """
    Фикстура для инициализации и завершения работы с веб-драйвером
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Тестовый случай, который проверяет вход в систему и дополнительно страницу профиля
def test_login_and_check_profile(browser):
    """
    Тестовый случай: вход в систему и проверка страницы профиля
    """
    def check_profile_page(browser):
        """
        Колбек-функция для проверки элементов на странице профиля
        """
        # Проверяем наличие элементов профиля
        assert browser.find_element_by_id("profile_name")
        assert browser.find_element_by_id("logout_button")

    # Вызываем функцию входа с колбеком для проверки профиля
    login_to_site(browser, after_login_callback=check_profile_page)

# Другой тестовый случай, использующий ту же логику входа, но с другой проверкой
def test_login_and_check_dashboard(browser):
    """
    Тестовый случай: вход в систему и проверка панели управления
    """
    def check_dashboard(browser):
        """
        Колбек-функция для проверки элементов на панели управления
        """
        # Проверяем наличие элементов панели управления
        assert browser.find_element_by_id("dashboard")

    # Вызываем функцию входа с колбеком для проверки панели управления
    login_to_site(browser, after_login_callback=check_dashboard)
'''

'''
Пояснения:
Функция login_to_site: 
Это основная функция, которая автоматизирует процесс входа в систему. 
Она принимает два параметра: 
browser (веб-драйвер) 
и after_login_callback (колбек-функция, которая будет вызвана после успешного входа).

Фикстура browser: 
Это фикстура pytest, 
которая инициализирует экземпляр веб-драйвера перед каждым тестом 
и закрывает его после выполнения теста.

Тестовые Случаи: 
test_login_and_check_profile и 
test_login_and_check_dashboard - 
это два тестовых случая, которые используют login_to_site 
для автоматизации входа. 
Каждый тест определяет свою колбек-функцию для выполнения специфичных проверок 
после входа в систему (проверка страницы профиля и панели управления соответственно).

Колбек-Функции в Тестах: 
В каждом тесте определена своя колбек-функция. 
Эти функции вызываются внутри login_to_site 
после успешного входа для выполнения дополнительных проверок.

Этот подход позволяет вам переиспользовать общий код 
(вход в систему) и легко расширять тесты с различными послевходовыми проверками, 
что улучшает организацию кода и уменьшает его дублирование.
'''



def filter_data(data, filter_function):
    """
    Фильтрует список данных, используя предоставленную функцию фильтрации.

    :param data: Список данных для фильтрации.
    :param filter_function: Функция, которая используется для фильтрации данных.
                            Должна принимать один элемент списка и возвращать
                            True, если элемент должен быть включен, иначе False.
    :return: Отфильтрованный список.
    """
    filtered_data = []
    for item in data:
        if filter_function(item):  # Вызов колбек-функции
            filtered_data.append(item)
    return filtered_data

# Пример использования
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Колбек-функция, которая возвращает True для четных чисел
def is_even(number):
    return number % 2 == 0

# Фильтрация данных с использованием колбек-функции is_even
filtered_even = filter_data(data, is_even)
print("Четные числа:", filtered_even)

# Колбек-функция, которая возвращает True для чисел больше 5
def is_greater_than_five(number):
    return number > 5

# Фильтрация данных с использованием колбек-функции is_greater_than_five
filtered_greater_than_five = filter_data(data, is_greater_than_five)
print("Числа больше пяти:", filtered_greater_than_five)

'''
Объяснение:

Функция filter_data: 
Эта функция принимает список data и функцию filter_function. 
Она проходит по всем элементам списка и использует filter_function 
для определения, должен ли элемент быть включен в отфильтрованный список.

Колбек-Функции:

is_even: 

Эта функция является колбеком, 
который определяет, является ли число четным. 
Она используется для фильтрации списка, 
чтобы оставить только четные числа.

is_greater_than_five: 

Этот колбек проверяет, больше ли число пяти. 
Он используется для фильтрации списка, чтобы оставить числа больше пяти.

Вызов filter_data с Разными Колбеками:

Первый вызов filter_data использует is_even для фильтрации, 
результатом чего является список четных чисел.

Второй вызов filter_data использует is_greater_than_five, 
и результатом является список чисел, больших пяти.

Этот пример показывает, 
как использование колбек-функций может сделать ваш код более модульным и гибким, 
позволяя легко изменять поведение функции без изменения её кода.
'''

