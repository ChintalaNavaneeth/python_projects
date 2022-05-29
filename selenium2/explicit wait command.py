from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")


driver.maximize_window()
driver.get("http://vtop1.vitap.ac.in:8080/onlineexam/processStudentLogin") # assuming url takes time to open
driver.find_element_by_id( "applnum").send_keys('2018747064')
driver.find_element_by_name("bdd").send_keys('04')
driver.find_element_by_name( "bmm").send_keys('04')
driver.find_element_by_name("byyyy").send_keys('2001')

time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='form-signin_v2']/div[2]/div/button").click() #explicit wait


#for clicking checkbox

#wait = WebDriverWait(driver,10)
#element = wait.until(EC,element_to_be_cliclable((By.XPATH,"XPLATH URL")))
#element.click()


wait = WebDriverWait(driver,10)
