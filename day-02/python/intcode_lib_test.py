import unittest 
from intcode_lib import return_four

class IntcodeLibTest(unittest.TestCase): 
  
    # Returns True or False.  
    def test(self):         
        self.assertTrue(True)

    def test2(self):
        self.assertTrue(return_four() == 4)
  
if __name__ == '__main__': 
    unittest.main() 
