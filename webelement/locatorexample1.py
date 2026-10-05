import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")

box=driver.find_element(By.ID,"APjFqb")
box.send_keys("how is weather today in noida!!!")
box.send_keys(Keys.ENTER)


time.sleep(5)
