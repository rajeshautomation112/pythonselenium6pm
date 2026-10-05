import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")

box=driver.find_element(By.CSS_SELECTOR,"#APjFqb")

print("The height and width of the box is ::",box.size)


print("The x and y coordinates of the box is ::",box.location)

r=box.rect

h=r['height']
print(r['height'])
print(r['width'])
print(r['x'])
print(r['y'])

print(box.get_attribute("class"))

time.sleep(5)

