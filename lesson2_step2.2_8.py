'''
Задание: загрузка файла
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
#Следующая строка работает не у всех, но так реально удобнее
from webdriver_manager.chrome import ChromeDriverManager
import time 
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("pipka@gmail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test2_2.2_6.txt')
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    # успеваем скопировать
    time.sleep(10)
    # закрываем браузер
    browser.quit()

# не забываем оставить пустую строку в конце файла
