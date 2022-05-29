import unittest
from selenium import webdriver

class  Test(unittest.TestCase):
    def testname(self):
        driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")
        driver.get("https://google.com")
        titlewedriver = driver.title
        #self.assertEqual("Goolge",titlewedriver,"web page title is not same")
        #driver.close()

        self.assertNotEqual("Gogle",titlewedriver,"both are same title")
        driver.close()
if __name__ == "__main__":
    unittest.main()