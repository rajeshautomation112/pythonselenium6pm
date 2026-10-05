import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.myntra.com/")


gen=driver.find_element(By.LINK_TEXT,"GENZ")

print(gen.location)
act=ActionChains(driver)

#act.move_to_element(gen).pause(2).click().perform()

act.move_by_offset(507,32).perform()
time.sleep(5)





