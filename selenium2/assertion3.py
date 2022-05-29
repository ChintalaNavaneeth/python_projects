import unittest
from selenium import webdriver

class simpletest(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")
        driver = None
        self.assertIsNone(driver)




if __name__ == "__main__":
    unittest.main()