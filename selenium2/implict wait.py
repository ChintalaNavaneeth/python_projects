from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")

driver.get("https://google.com") # assuming url takes time to open

driver.implicitly_wait(10) #waits for 10 seconds applicable for all elements, and only 1 timenat the beginning


#assert "Welcome: Mercury" in driver.title
driver.find_element_by_name("q").send_keys("mercury")
#driver.find_element_by_name("password").send_keys("mercury")
driver.find_element_by_name("btnK").click()