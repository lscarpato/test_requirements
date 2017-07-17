
import unittest

from functions.sum_function import SumFunction

class TestsDinamicDictionary(unittest.TestCase):
    
    def test_do_add_one( self):
        funcion_sum = SumFunction()
        result = funcion_sum.do_add_one(4)
        print result
        
if __name__ == '__main__':
    unittest.main()