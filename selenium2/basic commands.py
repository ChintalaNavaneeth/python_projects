from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Register.html")
print(driver.title) #returns title of the page
print(driver.current_url) # return current url of the page

driver.find_element_by_xpath("//*[@id='submitbtn']").click()

time.sleep(5)
#driver.close() # closes current browser
driver.quit()  # closes all open broswers