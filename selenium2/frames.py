from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")

driver.get()

driver.switch_to.frame("") #copy name
driver.find_element_by_link_text("").click()
driver.switch_to.default_content()
time.sleep(3)

driver.switch_to.frame("") #2nd r=frame name
driver.find_element_by_link_text("").click()
driver.switch_to.default_content()




