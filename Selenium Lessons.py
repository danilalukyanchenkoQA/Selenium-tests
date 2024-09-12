import time

from selenium import webdriver
driver = webdriver.Chrome()


# Управление навигацией браузера
driver.get("https://unsplash.com/")
driver.back()
driver.forward()
driver.refresh()
print("Все шаги теста 1 пройдены успешно!)")


driver.get("https://ru.wikipedia.org/")
url = driver.current_url    # Получаем текущий URL-адрес в переменную,
print("URL страницы: ", url) # Выводим значение переменной
assert url == "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0" , "Ошибка в URL"

current_tittle = driver.title # Записываем значение title в переменную current_title
print("Текущий заголовок: ", current_tittle) # Выводим значение переменной на экран
assert current_tittle == "Википедия — свободная энциклопедия", "Неверный заголовок"

# PAGE_SOURCE = driver.page_source # Записываем в переменную всю веб-страницу
# print(PAGE_SOURCE) # Печатаем HTML-код в терминал
print("Все шаги теста 2 пройдены успешно!)")


# Lesson 4 Home Work, использую браузер Фаерфоекс

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("https://vk.com/")
url = driver.current_url    # Получаем текущий URL-адрес в переменную,
tittleVK = driver.title # Записываем значение title в переменную title
print("Текущий заголовок: ", tittleVK) # Выводим значение переменной на экран
driver.get("https://dzen.ru/")
tittleYA = driver.title # Записываем значение title в переменную title
print("Текущий заголовок: ", tittleYA) # Выводим значение переменной на экран
driver.back()
assert tittleVK == "ВКонтакте | Добро пожаловать", "Неверный заголовок" # Делаем проверку на заголовок страницы
assert url == "https://vk.com/" , "Ошибка в URL" # Делаем проверку на URL страницы
driver.refresh()
print(driver.current_url)
driver.forward()
print(driver.current_url)
assert driver.current_url == "https://dzen.ru/" , "Ошибка в URL" # Делаем проверку на текущий URL страницы
print("Все шаги теста пройдены успешно!)")
print("Все шаги теста 3 пройдены успешно!)")


# Lesson 5 Поиск веб-элементов и ввод текста в поля

driver.get("http://localhost:3000/")
print("Открылся твой локальный стенд)")
driver.find_element("name", "user").send_keys("ваш email")
driver.find_element("name", "password").send_keys("ваш пароль")
driver.find_element("class name","css-1b7vft8-button").click()


# Записываем логин и пароль в переменную и пробуем еще раз залогиниться
email = driver.find_element("name", "user")
password = driver.find_element("name", "password")
email.send_keys("1")
password.send_keys("2")
print("Все шаги теста 4 пройдены успешно!)")


# Работа со списками элементов

elements = ["one", "two", "three"]
print(elements[0])


driver.get("http://localhost:3000/")
print(len(driver.find_elements("class name", "css-1riaxdn"))) # Если на странице несколько элементов с одинаковым классом, то выводим в консоль количество таких одинаковых элементов
print(driver.find_elements("class name","css-1riaxdn")[1]) # Выводим нужный нам элемент в консоли
driver.find_elements("class name","css-1riaxdn")[1].click() # Кликаем по нужному нам id элемента так как на странице элементов с таким class name несколько
print(("Все шаги теста 5 пройдены успешно)"))