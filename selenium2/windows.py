from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")

driver.maximize_window()
driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

print(driver.current_window_handle) #parent tab
handles = driver.window_handles # return all the handle values of open browser windows


for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=="Frames & windows":
        driver.close()

driver.quit()