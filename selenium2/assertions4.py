import unittest
class Test(unittest.TestCase):
    def testName(self):
        list=("python","selenium","java")
        #self.assertIn("python",list)  #returns true

        self.assertNotIn("c++",list) # returns true


if __name__ == "__main__":
    unittest.main()