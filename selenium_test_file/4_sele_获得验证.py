from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://www.126.com")

driver.maximize_window()

time.sleep(2)

print(driver.title)

print(driver.current_url)


time.sleep(2)

driver.close()