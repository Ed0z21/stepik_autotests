'''
Задание: ждем нужный текст на странице
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
#Следующая строка работает не у всех, но так реально удобнее
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    dfs = browser.find_element(By.ID, "book")
    dfs.click()
    x_element = browser.find_element(By.ID, "input_value")
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    x = int(x_element.text)
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    button = browser.find_element(By.ID, "solve")
    button.click()
finally:
    # успеваем скопировать код
    time.sleep(15)
    # закрываем браузер
    browser.quit()

# не забываем оставить пустую строку в конце файла
