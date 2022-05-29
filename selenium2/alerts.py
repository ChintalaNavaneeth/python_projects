from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")

driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
time.sleep(3)

#driver.switch_to_alert().accept() #closes alert window using ok button
driver.switch_to_alert().dismiss() #closes alert by using cancel button