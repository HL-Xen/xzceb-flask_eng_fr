import unittest

from translator import french_to_english, english_to_french

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(french_to_english(''), 'Hello') # test when Null is given as input the output is not 'Hello'.
        self.assertEqual(french_to_english('Bonjour'), 'Hello')  # test when 'Bonjour' is given as input the output is 'Hello'.       

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(english_to_french(''), 'Bonjour') # test when Null is given as input the output is not 'Bonjour.
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # test when 'Hello' is given as input the output is 'Bonjour'.       
        
unittest.main()