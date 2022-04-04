import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test_null(self):
        self.assertEqual(
            englishToFrench(None),
            '')

    def test_hello(self):
        self.assertEqual(
            englishToFrench('Hello'), 
            'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    def test_null(self):
        self.assertEqual(
            frenchToEnglish(None),
            '')

    def test_bonjour(self):
        self.assertEqual(
            frenchToEnglish('Bonjour'), 
            'Hello')

unittest.main()