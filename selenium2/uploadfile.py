from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")

driver.switch_to_frame(0)
driver.find_element_by_name("RESULT_FileUpload-10").send_keys(" file address")
