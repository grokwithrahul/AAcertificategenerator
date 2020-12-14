import unittest
import sys
sys.path.append("../certificategenerator/certificate.py")
import bin._tools as testmodule

class testThankyou(unittest.TestCase):
    names = ["", "a", "Rahul", "1234567890123456", "12345679012345678901234567890123456", None, 1, 5, 0.3, True]
    thickni = ["4", "4", "4", "4"]
    def testScaleThickness(self):
        for name in testThankyou.names:
            thickness = testmodule.optimalScale(name, 850)
            prit
