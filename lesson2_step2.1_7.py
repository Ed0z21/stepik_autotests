'''
Задание: поиск сокровища с помощью get_attribute
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
#Следующая строка работает не у всех, но так реально удобнее
from webdriver_manager.chrome import ChromeDriverManager
import time
import math


try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("http://suninjuly.github.io/get_attribute.html")
    x_element = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    x = int(x_element)
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    # успеваем скопировать код
    time.sleep(10)
    # закрываем браузер
    browser.quit()

# не забываем оставить пустую строку в конце файла