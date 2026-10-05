import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.myntra.com/")

search_box=driver.find_element(By.XPATH,"//input[@placeholder='Search for products, brands and more']")

search_box.send_keys("watches")
search_box.send_keys(Keys.ENTER)


driver.find_element(By.XPATH,"(//img[contains(@alt,'CMF by Nothing Watch Pro 2, 1.32')])[1]").click()


ids=driver.window_handles

# for i in ids:
#    print(i)
#

time.sleep(3)

driver.switch_to.window(ids[1])


driver.find_element(By.XPATH,"//div[text()='ADD TO BAG']").click()
time.sleep(4)




