import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")
driver.maximize_window()

def setUpModule(): #run before any class has sarted !remember it should not be inside any class
    print("Starting Tests ... ")


def tearDownModule():  # runs after any class has ended ! remember it should not be inside any class
    print("All tests are performed sucessfully in the class")

class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(self):   #setup method runs before every method starts
        print(" --- Test --- ")

    @classmethod
    def setUpClass(cls):
        print("opening application -- http://demo.automationtesting.in/Windows.html")
        driver.get("http://demo.automationtesting.in/Windows.html")#runs before all methods starts

    @classmethod
    def tearDownClass(cls):
        print("closing application") # runs after all methods ends
        driver.quit()

    @classmethod
    def tearDown(self):  #teardown method runs after every method ends
        print("Test performed sucessfully \n")

    def test_a_verify_title(self):
        print("Verify Title of the Page")
        tite =driver.title
        self.assertEqual("Frames & windows",tite,"Title is not same ")


    def test_b_verify_current_url(self):
        print("Verify current Url")
        url = driver.current_url
        self.assertEqual("http://demo.automationtesting.in/Windows.html",url,"Url is not same ")

    def test_c_click_element(self):
        print("Verify Click() element on the website")
        driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[0])

    def test_d_navigation(self):
        print("Verify Navigation between two Sites")

        driver.get("http://demo.automationtesting.in/Windows.html")
        print(driver.title)
        driver.get("http://google.com/")
        print(driver.title)
        driver.back()  # back button in broswer
        print(driver.title)
        driver.forward()  # forward command in browser
        print(driver.title)

    def test_e_radio_check(self):
        print("Verify the display,enable and selection of textbox and radio button/check box")
        driver.get("http://sme.spicejet.com/")
        email = driver.find_element_by_xpath("//*[@id='UserName']")
        print("Email Text Box Displayed : ",email.is_displayed())
        print("Email Text Box Enabled : ",email.is_enabled())
        time.sleep(2)
        password = driver.find_element_by_xpath("//*[@id='LoginPassword']")
        print("Password Text box is Displayed : ",password.is_displayed())
        print("Password Text Box Enabled ",password.is_selected())
        time.sleep(1)
        checkb = driver.find_element_by_xpath("//*[@id='flexCheckChecked']")
        print("Check box enabled ",checkb.is_selected())

if __name__ == "__main__":
    unittest.main()
