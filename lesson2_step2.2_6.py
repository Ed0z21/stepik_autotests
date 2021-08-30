'''
Задание на execute_script
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
#Следующая строка работает не у всех, но так реально удобнее
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

try:
    #Подключение вебдрайвера для открытия окна
    browser = webdriver.Chrome(ChromeDriverManager().install())
    #Переход по ссылке
    browser.get(link)
    #Написание функции для расчета задания
    x_element = browser.find_element(By.ID, "input_value")
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    x = int(x_element.text)
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    #Следующая строка должна отскроллить до видимости кнопки
    option2 = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    #Нажатие кнопки подтверждения
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
finally:
    #Отсечка закрытия окна
    time.sleep(10)
    #Закрытие окна
    browser.quit()