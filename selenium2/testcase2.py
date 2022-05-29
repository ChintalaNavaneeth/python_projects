import unittest
from selenium import webdriver

class searchenginestest(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://google.com")
        print("title of the page is " + self.driver.title)
        self.driver.close()



    def test_Bing(self):
        self.driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://bing.com")
        print("title of the page is " + self.driver.title)
        self.driver.close()

if __name__=="__main__":
    unittest.main()