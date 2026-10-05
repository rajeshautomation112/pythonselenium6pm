import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.myntra.com/")


links=driver.find_elements(By.XPATH,"")

print(len(links))


for i in links:
    print(i.get_attribute("href"))
    print(i.text)
