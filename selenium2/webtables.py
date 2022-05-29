from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")

driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")

rows = (len(driver.find_elements_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr")))
col = len(driver.find_elements_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr[1]/th"))

for r in range(2,rows+1):
    for c in range(1,col+1):
        value = driver.find_element_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr["+str(r)+"]/th["+str(c)+"]").text
        print(value,end='  ')
    print()