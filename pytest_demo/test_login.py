import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def browser_setup():
    op= Options()
    op.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=op)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


    yield driver
   # driver.quit()


def test_login_credentials(browser_setup):

        driver=browser_setup
       # driver.implicitly_wait(10)

        # fluent wait
        w=WebDriverWait(driver,timeout=20,poll_frequency=0.2,ignored_exceptions=[NoSuchElementException])

        w.until(ec.visibility_of_element_located((By.NAME,"username"))).send_keys("admin")
      #  driver.find_element(By.NAME,"username").send_keys("admin")

        driver.find_element(By.NAME,"password").send_keys("admin123")
        driver.find_element(By.TAG_NAME,"button").click()
        time.sleep(4)
        assert driver.find_element(By.XPATH,"//span[text()='Dashboard']").is_displayed()
        assert driver.find_element(By.XPATH, "//span[text()='Dashboard']").text == "Dashboard"

def demo():
    print("github demo")