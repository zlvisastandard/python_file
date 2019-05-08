from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://cn.bing.com/")

driver.find_element_by_id("sb_form_q").send_keys(r"今日新闻")

driver.find_element_by_id("sb_form_go").click()

time.sleep(3)


driver.close()
