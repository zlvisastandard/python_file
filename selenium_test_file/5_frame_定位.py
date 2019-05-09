from selenium import webdriver

import time

driver = webdriver.Chrome()

driver.get("file:///Users/zhangliang/PycharmProjects/python_file/selenium_test_file/frame_file.html")

time.sleep(2)

driver.switch_to_frame("if")

driver.find_element_by_id("kw").send_keys("selenium")

time.sleep(1)

driver.find_element_by_id("su").submit()

time.sleep(2)

driver.close()


