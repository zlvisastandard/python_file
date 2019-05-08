from  selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://www.5itest.cn/register")

time.sleep(4)

print(EC.title_contains("学习"))

time.sleep(2)

driver.close()