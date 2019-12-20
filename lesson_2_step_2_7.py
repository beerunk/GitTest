from selenium import webdriver
import time 
import math
import os
a = str(math.ceil(math.pow(math.pi, math.e)*10000))


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    #link = browser.find_element_by_link_text(a)
    #link.click()

    input1 = browser.find_element_by_tag_name("[name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("@Smolensk")
    
    input1 = browser.find_element_by_id("file")
    print(input1)
    #time.sleep(5)
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    print(current_dir)
    #time.sleep(5)
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    print(file_path)
    #time.sleep(5)
    input1.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла