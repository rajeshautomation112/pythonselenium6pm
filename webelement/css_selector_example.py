import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")

box=driver.find_element(By.CSS_SELECTOR,"#APjFqb")
#box.send_keys("fghiofcgvhbnjmk,")
# time.sleep(3)
# box.clear()
#
# time.sleep(3)
# driver.find_element(By.CSS_SELECTOR,"textarea[jsname='yZiJbe']").send_keys("hello how are you today!!!,")
#

time.sleep(5)