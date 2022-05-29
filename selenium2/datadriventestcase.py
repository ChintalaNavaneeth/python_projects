import xlutils
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")

driver.maximize_window()
driver.get("enter url")

path = (r"C:/Users/navan/OneDrive/Desktop/SaltBakerySales.xlsx")

rows = xlutils.getRowCount(path,'Location')

for r in rows(2,rows+1):
   username = xlutils.readData(path,'Location',r,1)
   password = xlutils.readData(path,'Location',r,2)

   driver.find_element_by_name("username").send_keys(username)
   driver.find_element_by_name("password").send_keys(password)

   driver.find_element_by_name("login").click()
   if driver.title == "find a flight: mercury tours":
       print("test is passed")
       xlutils.writeData(path,"Location",r,3,"sucess")
   else:
       print("test failed")
       xlutils.writeData(path,"Location",r,3,"failed")

driver.find_element_by_link_text("Home").click()

driver.close()