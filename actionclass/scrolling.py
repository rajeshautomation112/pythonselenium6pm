import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.myntra.com/")


act = ActionChains(driver)

#act.scroll_by_amount(0,2200).perform()


ref=driver.find_element(By.XPATH,"//p[text()=' EXPERIENCE MYNTRA APP ON MOBILE ']")

act.scroll_to_element(ref).perform()
time.sleep(2)
#act.scroll_by_amount(0,-200).perform()
time.sleep(4)
img=driver.find_element(By.XPATH,"//img[contains(@src,'4eabed')]")

time.sleep(3)
#print(img.is_displayed())
img.click()

time.sleep(5)