import unittest
from even_odd.even_odd import is_even

class TestEvenOdd(unittest.TestCase):
    
    def test_is_even_invalid_input(self):
        """Test invalid inputs raising ValueError."""
        with self.assertRaises(ValueError):
            is_even(2.3)
        with self.assertRaises(ValueError):
            is_even('gd')
        with self.assertRaises(ValueError):
            is_even(None)  
        with self.assertRaises(ValueError):
            is_even([])    
        with self.assertRaises(ValueError):
            is_even({}) 


    def test_is_even_even(self):
        """ Test even numbers returning True """
        self.assertTrue(is_even(4))
        self.assertTrue(is_even(10000))


    def test_is_even_odd(self):
        """ Test odd numbers returning False """
        self.assertFalse(is_even(5))
        self.assertFalse(is_even(99))


if __name__ == "__main__":
    unittest.main()