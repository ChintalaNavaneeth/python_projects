import unittest
from selenium import webdriver

class Test(unittest.TestCase):

    def testName(self):
        driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")
        driver.get("https://google.com")
        webtitle = driver.title
        #self.assertTrue(webtitle == "Google", "both are not same")

        self.assertFalse(webtitle == "Google"," both are same")
        driver.close()

if __name__ == "main":
    unittest.main()