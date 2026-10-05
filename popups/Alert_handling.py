import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Alerts.html")

driver.find_element(By.XPATH,"//button[contains(text(),'click the button to display an  alert box')]").click()

time.sleep(3)
al=driver.switch_to.alert

al.send_keys("raj")
al.accept()

time.sleep(6)