Создапние виртуального окружения (Если не используете PyCharm, если используете, то делать этого не нужно):


Виртуальное окружение нужно для изоляции проекта, чтобы все устанавливаемые библиотеки использовались только в рамках текущего проекта и не было конфликтов с другими зависимостями.

Первым делом создадим виртуальное окружение:
python3 -m venv venv

В результате, в директории проекта появится папка venv.

Теперь необходимо активировать окружение:
Mac OS / Linux:
source venv/bin/activate
Windows PowerShell:
venv/Scripts/activate.ps1

В результате, в терминале вы увидите префикс с названием окружения примерно такого формата:
Важно знать: окружение работает в рамках текущей сессии окна терминала, т.е если вы закроете терминал, то окружение снова нужно будет активировать.
Но если вы решили удалить папку venv, и пересоздать окружение, то сначала деактивируйте его командой:
deactivate

Установка Selenium и зависимостей:

1. Установка зависимостей - pip3 install selenium webdriver-manager
2. Импортируем драйвер - from selenium import webdriver
3. Установка Селениум - pip3 install selenium
4. установка библиотеки packaging - pip3 install packaging
5. Установить библиотеку webdriver-manager = pip3 install webdriver-manager

   Инициализация:

# Инициализация через Firefox

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

# или

from selenium import webdriver
driver = webdriver.Firefox()

# Инициализация через Chrome

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# или

from selenium import webdriver
driver = webdriver.Chrome()

