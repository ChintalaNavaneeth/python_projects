from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()

#how to find how many input boxes in the form???
x = driver.find_elements(By.CLASS_NAME,'text_field')
print(len(x))
#driver.quit()

#provide value into textbox

driver.find_element(By.ID,'RESULT_TextField-1').send_keys("NAVANEETH")
print(status)
driver.find_element(By.ID,'RESULT_TextField-2').send_keys("CHINTALA")
print(status)

#get status - use conditions

driver.close()