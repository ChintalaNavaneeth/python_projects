import unittest

class PaymentTest(unittest.TestCase):
    def test_paymentindollor(self):
        print("this is payment in dollor test")
        self.assertTrue(True)


    def test_paymentinrupees(self):
        print("this is payment in rupees test")
        self.assertTrue(True)

if __name__ == "__mainb__":
    unittest.main()