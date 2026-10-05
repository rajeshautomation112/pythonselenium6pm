import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")

time.sleep(3)
drop=driver.find_element(By.TAG_NAME,"select")

#object of the select class
sct=Select(drop)

print(sct.is_multiple)

op=sct.options

print("The total no.of country count are::",len(op))

# for i in op:
#     print(i.text)
#     i.click()

sct.select_by_index(2)
time.sleep(3)
sct.select_by_visible_text("Argentina")
time.sleep(3)
sct.select_by_value("AFG")

time.sleep(5)