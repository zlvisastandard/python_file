from selenium import webdriver

import time

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

size = driver.find_element_by_id("kw").size

print(size)

test = driver.find_element_by_id("cp").text

print(test)

attr = driver.find_element_by_id("kw").get_attribute("name")

print(attr)

result = driver.find_element_by_id("kw").is_displayed()

print(result)


time.sleep(2)

driver.close()