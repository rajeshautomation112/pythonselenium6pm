import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#
# kd=driver.find_element(By.LINK_TEXT,"KIDS")
#
# print(kd.text)
#
# print(kd.tag_name)
#
# print(kd.is_displayed())
# print(kd.is_enabled())
# print(kd.is_selected())
# print(kd.click())

driver.refresh()
time.sleep(7)

t=driver.find_element(By.PARTIAL_LINK_TEXT,"OrangeHRM")
print(t.text)

print(t)
time.sleep(6)

