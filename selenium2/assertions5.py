import unittest

class Test(unittest.TestCase):
    def testname(self):
        list = (1,2,3,4,5,6,7,8,9)
        #self.assertGreater(5,4,"not greater")
        #self.assertGreaterEqual(5,6,"not equal")
        #self.assertLess(1,2,"false statement")
        self.assertLessEqual(2,4,"false statement")




if __name__ == "__main__":
    unittest.main()