from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")
#driver.get("http://newtours.demoaut.com/")

print(driver.title)   #title of the page
print(driver.current_url) #gets url
print(driver.page_source) # returns html code for the page
driver.close()  # close browser
