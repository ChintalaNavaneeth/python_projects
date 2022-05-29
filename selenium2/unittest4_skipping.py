import unittest

class Apptesting(unittest.TestCase):

    @unittest.SkipTest   #1.using decorator
    def test_search(self):
        print("testing search")

    @unittest.skip("program not ready so iam skipping this test")   #skipping with reason
    def test_advancesearch(self):
        print("testing Advance search")

    @unittest.skipIf(1==1, " this is condtion skip example+") # skipping with condition
    def test_prepaidrecharge(self):
        print("testing prepaid recharge")

    def test_postpaidrecharge(self):
        print("testing postpaaid recharge")

    def test_loginbygmail(self):
        print("testing login by gmail")

    def test_loginbytwitter(self):
        print("testing twitter login")


if __name__ == "__main":
    unittest.main()