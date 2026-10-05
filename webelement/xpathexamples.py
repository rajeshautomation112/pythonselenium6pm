import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.myntra.com/")

driver.find_element(By.XPATH,"//span[text()='Profile']").click()

time.sleep(2)
driver.find_element(By.XPATH,"//a[text()='login / Signup']").click()

time.sleep(5)