import unittest 
from intcode_lib import process_intcode

class IntcodeLibTest(unittest.TestCase): 
    def testProcessIntcode1(self):
        intcode_input = [1,9,10,3,2,3,11,0,99,30,40,50]
        intcode_output = [3500,9,10,70,2,3,11,0,99,30,40,50]
        self.assertTrue(process_intcode(intcode_input) == intcode_output)

    def testProcessIntcode2(self):
        intcode_input = [1,0,0,0,99]
        intcode_output = [2,0,0,0,99]
        self.assertTrue(process_intcode(intcode_input) == intcode_output)

    def testProcessIntcode3(self):
        intcode_input = [2,3,0,3,99]
        intcode_output = [2,3,0,6,99]
        self.assertTrue(process_intcode(intcode_input) == intcode_output)

    def testProcessIntcode4(self):
        intcode_input = [2,4,4,5,99,0]
        intcode_output = [2,4,4,5,99,9801]
        self.assertTrue(process_intcode(intcode_input) == intcode_output)


    def testProcessIntcode5(self):
        intcode_input = [1,1,1,4,99,5,6,0,99]
        intcode_output = [30,1,1,4,2,5,6,0,99]
        self.assertTrue(process_intcode(intcode_input) == intcode_output)

if __name__ == '__main__': 
    unittest.main() 
