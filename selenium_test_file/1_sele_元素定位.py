from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("file:///Users/zhangliang/PycharmProjects/python_file/selenium_test_file/link.html")

driver.find_element_by_link_text("贴吧>").click()

# driver.find_element_by_name("tj_trtieba").click()

time.sleep(3)

driver.close()


# driver.get("http://www.baidu.com")
#
# # driver.set_window_size(400,800)
#
# driver.maximize_window()
#
# driver.find_element_by_id("kw").send_keys("新闻")
#
# res = driver.find_element_by_id("su")
#
# res.submit()
#
# time.sleep(2)

# driver.back()
#
# time.sleep(1.5)
#
# driver.forward()
#
# time.sleep(2)
#
# driver.refresh()
#
# driver.get_screenshot_as_file("/Users/zhangliang/PycharmProjects/python_file/selenium_test_file/1.png")
#
# time.sleep(2)

# driver.close()