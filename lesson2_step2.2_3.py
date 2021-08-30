'''
Задание: работа с выпадающим списком
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
#Следующая строка работает не у всех, но так реально удобнее
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects1.html"

try:
    #Подключение вебдрайвера для открытия окна
    browser = webdriver.Chrome(ChromeDriverManager().install())
    #Переход по ссылке
    browser.get(link)
    #Поиск первого члена суммы, перевод его из веб-объекта в текст и перевод в число для последующей операции сложения
    first_part = int((browser.find_element(By.ID, "num1")).text)
    #Поиск второго члена суммы, перевод его из веб-объекта в текст и перевод в число для последующей операции сложения
    second_part = int((browser.find_element(By.ID, "num2")).text)
    #Нахождение суммы первого и второго члена, перевод в строку (текст)
    final_part = str((first_part) + (second_part))
    #Открытие выпадающего списка
    select = Select(browser.find_element(By.ID, "dropdown"))
    #Выбор из выпадающего списка того элемента, который равен сумме первого и второго члена в заголовке
    select.select_by_value(final_part)
    #Нажатие кнопки подтверждения
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
finally:
    #Отсечка закрытия окна
    time.sleep(10)
    #Закрытие окна
    browser.quit()