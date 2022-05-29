import unittest

from Package1.TC_login import LoginTest
from Package1.TC_signup import SigupTest

from Package2.TC_paymenttest import PaymentTest
from Package2.TC_paymentreturns import PaymentReturnTest


#to get all the test from LoginTest, SignupTest, PaymentTest, PaymentRetuernTest

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2= unittest.TestLoader().loadTestsFromTestCase(SigupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnTest)

#creating test suites
sanityTestSuite = unittest.TestSuite((tc1,tc2))
#unittest.TextTestRunner().run(sanityTestSuite)
print("--------------------------------")
functionaltestsuite =  unittest.TestSuite((tc3))
#unittest.TextTestRunner().run(functionaltestsuite)
print("--------------------------------")
mastertestsuite =  unittest.TestSuite((tc3,tc2,tc1,tc4))
unittest.TextTestRunner(verbosity=2).run(mastertestsuite)