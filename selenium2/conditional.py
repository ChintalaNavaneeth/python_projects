from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")
driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")

ele=driver.find_element_by_name("search_query")
print(ele.is_displayed())   #returns true or false
print(ele.is_enabled())  #returns is enable dor not

ele.send_keys("Faded")

driver.find_element_by_name("submit_search").click()
roundradio = driver.find_element_by_css_selector("input[value=roundtrip]")  #radio buttons use value insted of name
print(roundradio.is_selected()) # print status of radio button