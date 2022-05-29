from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Register.html")
print(driver.title)
driver.get("http://18mis7042.infinityfreeapp.com/home.html")
print(driver.title)
driver.back() # back button in broswer
print(driver.title)
driver.forward() #forward command in browser
print(driver.title)
driver.close()