import time
import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.yatra.com/")
time.sleep(3)
# driver.find_element(By.XPATH,"//p[contains(text(),'I have work experience')]").click()
#
time.sleep(4)
# driver.find_element(By.CSS_SELECTOR,"input[type='file']").send_keys(r"C:\Users\Administrator\Desktop\hello.pdf")


#pyautogui.write("admin")

pyautogui.press("tab")

#pyautogui.write("admin")

pyautogui.press("enter")


time.sleep(6)

