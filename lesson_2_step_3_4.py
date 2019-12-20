from selenium import webdriver
import time
import math
import capcha_bot

#def calc(x):
  #return str(math.log(abs(12*math.sin(int(x)))))

try: 
    
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    #confirm = browser.switch_to.alert
    #confirm.accept()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = capcha_bot.calc(x)
    
    input1 = browser.find_element_by_class_name('form-control')
    input1.send_keys(y)
    

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()