import unittest

from translator import french_to_english, english_to_french

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(''), '') # test when Null is given as input the output is None.
        self.assertEqual(french_to_english('Bonjour'), 'Hello')  # test when 'Bonjour' is given as input the output is 'Hello'.       

class TestDouble(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(''), '') # test when Null is given as input the output is None.
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # test when 'Hello' is given as input the output is 'Bonjour'.       
        
unittest.main()