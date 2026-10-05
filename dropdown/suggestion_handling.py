import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.yatra.com/")

# time.sleep(5)
# dep=driver.find_element(By.XPATH,"//p[text()='Departure From']")
# dep.click()
#
# time.sleep(3)
# driver.find_element(By.ID,"input-with-icon-adornment").send_keys("no")


#sugg=driver.find_elements(By.XPATH,"//div[@class='MuiStack-root css-wu34vq']//div[@class='MuiBox-root css-31l7gp']")


driver.find_element(By.XPATH,"//span[text()='Economy']").click()



time.sleep(5)

su=driver.find_elements(By.XPATH,"//ul[@class='css-lazo4l']/li")
time.sleep(2)
su[1].click()
#print("The total no. of suggestions are!!!",len(sugg))


#driver.find_element(By.XPATH,"//div[@class='MuiBox-root css-31l7gp']//p[text()='Nottingham']").click()
#sugg[1].click()
#for s in sugg:
    #print(s.text)
    #
    # if s.text=="Noida":
    #     time.sleep(4)
    #     s.click()
    #     break
time.sleep(8)
