from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

driver.maximize_window()

driver.find_element_by_id("kw").send_keys("selenium")

time.sleep(2)

driver.find_element_by_id("su").send_keys(Keys.ENTER)

# driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

# time.sleep(2)
#
# driver.find_element_by_id("kw").send_keys(Keys.SPACE)
#
# time.sleep(1)
#
# driver.find_element_by_id("kw").send_keys(u"教程")

# time.sleep(2)

# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')

# time.sleep(2)

# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')

time.sleep(2)

driver.find_element_by_class_name("toindex").send_keys(Keys.TAB)

time.sleep(2)



driver.close()


