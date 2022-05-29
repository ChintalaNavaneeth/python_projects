from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")

driver.get("https://www.amazon.in")

#capture all cookies created by the browser

cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

#add new cookie to browser
cookie = {'name': 'mycookie', 'value':'123654789'}
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

driver.delete_cookie('mycookie')
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

driver.delete_all_cookies()
print(len(cookies))