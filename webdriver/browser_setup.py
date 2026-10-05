import time

from selenium import webdriver
driver = webdriver.Edge()
driver.maximize_window()
driver.get("http://google.com")

print("The title of the window is :::",driver.title)
print("The current page url is :::",driver.current_url)

# driver.back()
# time.sleep(1)
# driver.forward()
# time.sleep(1)
# driver.refresh()

# print("The x and y coordinate of the window is ::",driver.get_window_position())
# print("The height and width of the window is ::",driver.get_window_size())
#
#
# driver.set_window_size(100, 200)
#
# driver.set_window_position(100, 200)
#
#
# rec=driver.get_window_rect()
#
# print(len(rec))
#
# print(rec.get("width"))
# print(rec.get("height"))
# print(rec.get("x"))
# print(rec.get("y"))


print("The window handle is :::;"+driver.current_window_handle)

time.sleep(6)

