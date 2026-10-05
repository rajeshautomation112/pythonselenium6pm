import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.myntra.com/")

#
#
#
# fr=driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
#
#
# time.sleep(4)
#
# driver.switch_to.frame(fr)
# ball=driver.find_element(By.XPATH,"//img[@alt='The chalet at the Green mountain lake']")
#
#
# basket=driver.find_element(By.ID,"trash")
#
act =ActionChains(driver)
#
# act.drag_and_drop(ball,basket).perform()
# time.sleep(4)
# driver.switch_to.default_content()
#
# driver.find_element(By.XPATH,"//a[text()='CheatSheets']").click()

#act.scroll_by_amount(0,3000).perform()

r=driver.find_element(By.XPATH,"//p[text()=' EXPERIENCE MYNTRA APP ON MOBILE ']")

act.scroll_to_element(r).perform()
time.sleep(8)