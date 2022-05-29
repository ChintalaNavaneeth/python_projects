from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")

driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")

source_element = driver.find_element_by_id("draggable")
target_element = driver.find_element_by_id("droppable")

actions = ActionChains(driver)

actions.drag_and_drop(source_element,target_element).perform()# performs drag and drop
