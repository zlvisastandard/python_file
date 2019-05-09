from selenium import webdriver

import time


driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

seach = driver.current_window_handle

driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerQrcodeBtn"]').click()

time.sleep(2)

all_handles = driver.window_handles

for i in all_handles:
    if i != seach:
        print("注册窗口")
        driver.find_element_by_id("TANGRAM__PSP_10__footerQrcodeBtn")
        driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("18756927780")
        driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("love340827")
        driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
driver.close()