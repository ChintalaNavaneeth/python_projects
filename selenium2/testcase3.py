import unittest


def setUpModule(): #run before any class has sarted !remember it should not be inside any class
    print("setup module")

def tearDownModule():  # runs after any class has ended ! remember it should not be inside any class
    print("teardoen module")

class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(self):   #setup method runs before every method starts
        print("this is login test")

    @classmethod
    def tearDown(self):  #teardown method runs after every method ends
        print("this is logout")

    @classmethod
    def setUpClass(cls):
        print("opening application") #runs before all methods starts

    @classmethod
    def tearDownClass(cls):
        print("close application") # runs after all methods ends



    def test_search(self):
        print("this is search test")

    def test_advancedtest(self):
        print("this is advanced search test")

    def test_prepaidRecharge(self):
        print("this is prepaid recharge")

    def test_postpaidRecharge(self):
        print("this is postpaid recharge")

if __name__ == "__main__":
    unittest.main()
