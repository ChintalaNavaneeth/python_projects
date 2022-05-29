import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")
driver.maximize_window()

def setUpModule(): #run before any class has sarted !remember it should not be inside any class
    print("Starting Tests ... ")
    driver.get("https://www.techlistic.com/p/selenium-practice-form.html")


def tearDownModule():  # runs after any class has ended ! remember it should not be inside any class
    print("All tests are performed sucessfully in the class")

class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(self):   #setup method runs before every method starts
        print(" --- Test --- ")

    @classmethod
    def setUpClass(cls):
        print("opening application -- https://www.techlistic.com/p/selenium-practice-form.html")

    @classmethod
    def tearDownClass(cls):
        print("closing application") # runs after all methods ends
        driver.quit()

    @classmethod
    def tearDown(self):  #teardown method runs after every method ends
        print("Test performed sucessfully \n")


    def test_implicitwait(self):
        print("Test = 1 : Implicit wait Test")
        driver.get("https://www.techlistic.com/p/selenium-practice-form.html") # assuming url takes time to open
        driver.implicitly_wait(10) #waits for 10 seconds applicable for all elements, and only 1 timenat the beginning

    def test_inputboxes(self):
        print("Test = 2 : Input boxes Test")
        driver.find_element_by_xpath("//*[@id='post-body-3077692503353518311']/div/div/div[3]/input").click()
        print(driver.find_element_by_xpath("//*[@id='post-body-3077692503353518311']/div/div/div[3]/input").is_enabled())
        driver.find_element_by_xpath("//*[@id='post-body-3077692503353518311']/div/div/div[3]/input").send_keys("VIT")
        time.sleep(3)

    def test_radiobuttons(self):
        print("Test = 3 : Radio buttons Test")
        driver.find_element_by_xpath("//*[@id='sex-0']").click() #male radio button
        driver.find_element_by_xpath("//*[@id='sex-1']").click() # female radio button
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='exp-0']").click() #radio button 1
        driver.find_element_by_xpath("//*[@id='exp-1']").click() #radio button 2
        driver.find_element_by_xpath("//*[@id='exp-2']").click() #radio button 3
        driver.find_element_by_xpath("//*[@id='exp-3']").click() #radio button 4
        driver.find_element_by_xpath("//*[@id='exp-4']").click() #radio button 5
        driver.find_element_by_xpath("//*[@id='exp-5']").click() #radio button 6
        driver.find_element_by_xpath("//*[@id='exp-6']").click() #radio button 7
        time.sleep(3)

    def test_checkbox(self):
        print("Test = 4 : Check box test")
        driver.find_element_by_id('profession-1').click() # profession automation tester checkbox
        driver.find_element_by_id("tool-2").click() # selenium web driver check box
        time.sleep(3)

    def test_dropbox(self):
        print("Test = 5 : Drop box test")
       # driver.find_elements_by_name("continents").click()
        driver.find_element_by_xpath("//*[@id='continents']/option[7]").click()
        time.sleep(3)


    def test_explicitwait(self):
        print("Test = 6 : Explit wait ")
        try:
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.presence_of_element_located((By.ID, "submit")))
        finally:
            print(" ")


if __name__ == "__main__":
    unittest.main()
