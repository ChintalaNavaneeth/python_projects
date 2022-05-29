from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


chromeoptions = Options()
#if you want to change  download file directory from chrome
#chromeoptions.add_experimental_option("prefs",("download.default_directory":"Download address"))

driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe",chrome_options=chromeoptions)
driver.maximize_window()
driver.get("http://demo.automationtesting.in/FileDownload.html")

#Download text file
driver.find_element_by_id("textbox").send_keys("download text file")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()


#Download pdf file
driver.find_element_by_id("pdfbox").send_keys("download text file")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()

time.sleep(3)
driver.close()

