'''Задание на уникальность селекторов.
    Тестируется две страницы, на одной будет Ок, на другой будет краш
'''
#Импорт всего-всего
from selenium import webdriver
#Через By как-то сподручнее
from selenium.webdriver.common.by import By
#Следующая строка работает не у всех, но так реально удобнее
from webdriver_manager.chrome import ChromeDriverManager
import time 
#Забиваем ссыль
link1 = "http://suninjuly.github.io/registration1.html" #Работает
link2 = "http://suninjuly.github.io/registration2.html" #Крашится
#Пробуем решить задачку
try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link2)
    #Сначала мне казалось, что использовать XPATH - это мазохизм, но теперь я люблю его^_^
    input1 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control first"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control second"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control third"]')
    input3.send_keys("stepik@lessons.org")
    input4 = browser.find_element(By.XPATH, '//div[@class="second_block"]//input[@class="form-control first"]')
    input4.send_keys("320-80-80")
    input5 = browser.find_element(By.XPATH, '//div[@class="second_block"]//input[@class="form-control second"]')
    input5.send_keys("Санкт-Петербург")
    #Оставляем время на посмотреть:
    time.sleep(2)
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    #Отсечка на закрытие страницы
    time.sleep(10)
    #Закрытие браузера - обязательно
    browser.quit()

# Пустая строчка
