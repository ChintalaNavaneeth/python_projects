import unittest

class SigupTest(unittest.TestCase):
    def test_signbyemail(self):
        print("this is signup by email test")
        self.assertTrue(True)

    def test_signupbytwitter(self):
        print("this is signup by twitter test")
        self.assertTrue(True)

    def test_signupbyfacebook(self):
        print("this is signup by facebook test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()