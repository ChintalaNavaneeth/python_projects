from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")

driver.maximize_window()
driver.get("http://opensource-demo.orangehrmlive.com/")
driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys("Admin")
driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys("admin123")
driver.find_element_by_xpath("//*[@id='btnLogin']").click()

admin = driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
usermgmt = driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
users = driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")


#using mouse hover using action chain class
actions = ActionChains(driver)
actions.move_to_element(admin).move_to_element(usermgmt).move_to_element(users).click().perform()

time.sleep(3)
driver.close()
