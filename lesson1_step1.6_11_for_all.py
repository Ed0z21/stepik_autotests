'''Задание на уникальность селекторов.
    Тестируется две страницы, на одной будет Ок, на другой будет краш
'''
#Импорт всего-всего
from selenium import webdriver
#Через By как-то сподручнее
from selenium.webdriver.common.by import By
#Следующая строка работает не у всех, но так реально удобнее
#from webdriver_manager.chrome import ChromeDriverManager
import time 
#Забиваем ссыль
link1 = "http://suninjuly.github.io/registration1.html" #Работает
link2 = "http://suninjuly.github.io/registration2.html" #Крашится
#Пробуем решить задачку
try:
    browser = webdriver.Chrome()
    browser.get(link1)
    #Сначала мне казалось, что использовать XPATH - это мазохизм, но теперь я люблю его^_^
    browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control first"]').send_keys("Ivan")
    browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control second"]').send_keys("Petrov")
    browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control third"]').send_keys("stepik@lessons.org")
    browser.find_element(By.XPATH, '//div[@class="second_block"]//input[@class="form-control first"]').send_keys("320-80-80")
    browser.find_element(By.XPATH, '//div[@class="second_block"]//input[@class="form-control second"]').send_keys("Санкт-Петербург")
    browser.find_element(By.CSS_SELECTOR, "button").click()
    time.sleep(2)
finally:
    #Отсечка на закрытие страницы
    time.sleep(10)
    #Закрытие браузера - обязательно
    browser.quit()

# Пустая строчка
