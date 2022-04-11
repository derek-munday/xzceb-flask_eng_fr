import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test_null(self):
        self.assertEqual(
            english_to_french(None),
            '')

    def test_hello(self):
        self.assertEqual(
            english_to_french('Hello'), 
            'Bonjour')
        self.assertNotEqual(
            english_to_french('Hello'),
            'Hello'
        )

class TestFrenchToEnglish(unittest.TestCase):
    def test_null(self):
        self.assertEqual(
            french_to_english(None),
            '')

    def test_bonjour(self):
        self.assertEqual(
            french_to_english('Bonjour'), 
            'Hello')
        self.assertNotEqual(
            french_to_english('Bonjour'),
            'Bonjour'
        )

unittest.main()