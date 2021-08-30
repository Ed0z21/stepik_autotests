'''
Задание: переход на новую вкладку
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
#Следующая строка работает не у всех, но так реально удобнее
from webdriver_manager.chrome import ChromeDriverManager
import time
import math
import os

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element(By.ID, "input_value")
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    x = int(x_element.text)
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
finally:
    # успеваем скопировать код
    time.sleep(10)
    # закрываем браузер
    browser.quit()

# не забываем оставить пустую строку в конце файла
