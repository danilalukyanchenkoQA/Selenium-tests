import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("https://unsplash.com/")
time.sleep(5) # В качестве аргумента принимает кол-во секунд для паузы



