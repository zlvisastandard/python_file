from selenium import webdriver

import time

from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

#鼠标右击事件
# driver.get("http://yunpan.360.cn")
# time.sleep(2)
# right_click = driver.find_element_by_name("account")
# ActionChains(driver).context_click(right_click).perform()
# time.sleep(2)

#鼠标悬停事件
# driver.get("http://www.baidu.com")
# time.sleep(2)
# # move_above = driver.find_element_by_name("tj_settingicon")
# # above = driver.find_element_by_class_name("pf")
# above = driver.find_element_by_link_text("设置")
# time.sleep(2)
# ActionChains(driver).move_to_element(above).perform()
# time.sleep(2)


driver.close()