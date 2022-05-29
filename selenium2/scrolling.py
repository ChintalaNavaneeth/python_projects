from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")

driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")

#driver.execute_script("window.scrollBy(0,500)","") #scrolling till 500 pixels
#time.sleep(5)

#p = driver.find_element_by_xpath("//*[@id='q22']/div/a")#scroll by element
#driver.execute_script("arguments[0].scrollIntoView();",p)
#time.sleep(10)

#to scroll till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(3)
driver.close()
