import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoapps.qspiders.com/ui/clickHold?sublist=0")

time.sleep(3)
cir=driver.find_element(By.ID,"circle")

act=ActionChains(driver)

act.click_and_hold(cir).release().perform()
time.sleep(7)




