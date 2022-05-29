from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")
driver.get("http://www.edureka.co/")

#driver.save_screenshot(r"C:/Users/navan/OneDrive/Desktop/hmo.png")
driver.get_screenshot_as_file(r"C:/Users/navan/OneDrive/Desktop/hmo2.png")
