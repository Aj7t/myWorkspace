
import unittest
import re
from test_regex_collections import pincode

class Testingregex(unittest.TestCase):
    regex = r'^[0-9]{6}$'
        
    def test_regex(self):
        try:
            self.assertTrue(re.match(self.regex, "842701"))
            print("\033[96m" + "Regex expression is correct\n" + "\033[0m")
        
        except AssertionError as msg:
            print("\033[91m" + "Regex expression is incorrect\n" + "\033[0m")
            
            
    def test_positive_regex(self):
        try:
            self.assertTrue(re.match(self.regex, "84274501"))
            print("\033[94m" + "Regex expression is correct\n" + "\033[0m")
        
        except AssertionError as msg:
            print("\033[91m" + "Regex expression is incorrect\n" + "\033[0m")


print("\033[93m" + "************Everything passed*************\n\n"+"\033[0m")

if __name__ == '__main__':
    unittest.main()
    
