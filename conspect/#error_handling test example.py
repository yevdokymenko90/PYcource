#error_handling test example

from playwright.sync_api import sync_playwright
from playwright._impl._api_types import Error

def test_login():
    try:
        with sync_playwright() as p:
            # Запуск браузера
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            # Открытие страницы
            page.goto("https://the-internet.herokuapp.com/login")

            # Ввод данных пользователя
            page.fill("input#username", "tomsmith")
            page.fill("input#password", "SuperSecretPassword!")

            # Нажатие кнопки входа
            page.click("button[type='submit']")

            # Проверка успешного входа
            success_message = page.wait_for_selector("div#flash")
            assert "You logged into a secure area!" in success_message.text_content()

            # Закрытие браузера
            browser.close()

    except Error as e:
        print(f"Произошла ошибка при выполнении теста: {e}")
        if browser:
            browser.close()

if __name__ == "__main__":
    test_login()


'''
В этом коде:

Используется sync_playwright для синхронной работы с Playwright.
Открывается браузер и переходит на страницу входа.
Вводятся данные для входа и нажимается кнопка входа.
Ожидается появление сообщения об успешном входе и проверяется его содержание.
При возникновении исключения Error в процессе выполнения теста, 
это исключение будет перехвачено и обработано в блоке except, а браузер закрыт.


Активный выбор - это скрипт на Python, 
который использует библиотеку Playwright 
для автоматизации действий в браузере для тестирования. 
Этот скрипт конкретно тестирует функциональность входа на веб-страницу.

Функция `test_login` - это основная функция в этом скрипте. 
Она использует блок `try` для попытки автоматизации шагов в браузере 
и блок `except` для обработки любых исключений, которые происходят в процессе.

Внутри блока `try` используется менеджер контекста `sync_playwright` 
для запуска экземпляра Playwright. 
Строка `p.chromium.launch(headless=True)` 
запускает новый экземпляр браузера Chromium без графического интерфейса. 
Браузер без графического интерфейса - 
это веб-браузер без графического интерфейса, 
который полезен для автоматизированного тестирования.

В браузере открывается новая страница с помощью `browser.new_page()`, 
а затем функция `page.goto` переходит на указанный URL.

Функция `page.fill` используется для заполнения полей 
имени пользователя и пароля на странице входа. 
Затем функция `page.click` используется для нажатия кнопки отправки.

После попытки входа скрипт ожидает появления сообщения 
об успехе на странице с помощью 
`page.wait_for_selector("div#flash")`. 
Оператор `assert` проверяет, 
что текст сообщения об успехе включает "You logged into a secure area!".

Если во время этих шагов происходит какая-либо ошибка, 
блок `except` перехватывает исключение и выводит сообщение об ошибке. 
Он также проверяет, существует ли объект `browser`, и если да, то закрывает браузер.

Строка `if __name__ == "__main__":` в конце скрипта - это общий идиом Python. 
Если этот скрипт запускается напрямую 
(а не импортируется как модуль), эта строка гарантирует, 
что будет вызвана функция `test_login`.


The active selection is a Python script that uses 
the Playwright library to automate browser actions for testing purposes. 
This script specifically tests the login functionality of a web page.

The `test_login` function is the main function in this script. 
It uses a `try` block to attempt the browser automation steps, 
and an `except` block to handle any exceptions that occur during the process.

Inside the `try` block, the `sync_playwright` 
context manager is used to start a Playwright instance. 
The `p.chromium.launch(headless=True)` 
line launches a new instance of a headless Chromium browser. 
A headless browser is a web browser without a graphical user interface, 
which is useful for automated testing.

A new page is opened in the browser with `browser.new_page()`, 
and then the `page.goto` function navigates to the specified URL.

The `page.fill` function is used to fill in 
the username and password fields on the login page. 
The `page.click` function is then used to click the submit button.

After the login attempt, 
the script waits for a success message to appear on the page with 
`page.wait_for_selector("div#flash")`. 
The `assert` statement checks that 
the success message text includes "You logged into a secure area!".

If any error occurs during these steps, 
the `except` block catches the exception and prints an error message.
It also checks if the `browser` object exists, and if so, 
closes the browser.

The `if __name__ == "__main__":` 
line at the end of the script is a common Python idiom. 
If this script is run directly (as opposed to being imported as a module), 
this line ensures that the `test_login` function is called.

'''

