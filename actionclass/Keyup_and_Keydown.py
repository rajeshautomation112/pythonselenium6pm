import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.myntra.com/")


act=ActionChains(driver)

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()


act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

search=driver.find_element(By.CSS_SELECTOR,"[class='desktop-searchBar']")
act.key_down(Keys.CONTROL,search).send_keys("v").key_up(Keys.CONTROL).perform()

time.sleep(5)
