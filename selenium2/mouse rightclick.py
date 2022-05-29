from selenium import webdriver
from selenium.webdriver import ActionChains
import time


driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")

driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")
element = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")

actions = ActionChains(driver)
#right click action
actions.context_click(element).perform()