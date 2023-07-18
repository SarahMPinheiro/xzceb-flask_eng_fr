import unittest
from translator import french_to_english
from translator import english_to_french
class TestE2F(unittest.TestCase):
    """English to French tests"""
    def test1(self):
        try:
         # Test Hello returns Bonjour
            self.assertEqual(english_to_french('hello'), 'bonjour')
         # Test Hello does not return Hello
            self.assertNotEqual(english_to_french('hello'), 'hello')
        except AssertionError:
            print('pepitoooo' != 'bonjour')

class TestF2E(unittest.TestCase):
    """Frecnh to English tests"""
    def test2(self):
        try:
        # Test Hello returns Bonjour
            self.assertEqual(french_to_english('bonjour'), 'hello')
        # Test Hello does not return Hello
            self.assertNotEqual(french_to_english('bonjour'), 'bonjour') 
        except AssertionError:
            print('bonjour' != 'hello')
unittest.main()
