import unittest
from src.palindrome import is_palindrome 

class TestPalindrome(unittest.TestCase):
    def test_is_palindrome_Noneまたは空文字またはスペースだけの場合はFalse(self):
        self.assertEqual(False, is_palindrome(None))
        self.assertEqual(False, is_palindrome(''))
        self.assertEqual(False, is_palindrome('    '))
        self.assertEqual(False, is_palindrome('　　  '))    # 半角全角スペース混在

    def test_is_palindrome_大文字小文字が異なる場合はFalse(self):
        self.assertEqual(False, is_palindrome('aaabbbAAA'))

    def test_is_palindrome_文字列中に含まれるスペースは評価対象(self):
        self.assertEqual(False, is_palindrome('たけやぶ やけた'))   # 半角スペース
        self.assertEqual(False, is_palindrome('たけ　やぶやけた'))  # 全角スペース
        self.assertEqual(False, is_palindrome(' たけやぶやけた　'))  # 半角と全角スペース

    def test_is_palindrome_True(self):
        self.assertEqual(True, is_palindrome('たけやぶやけた'))
        self.assertEqual(True, is_palindrome('moooom'))
        self.assertEqual(True, is_palindrome(' 　たけ やぶや けた　 ')) # 半角と全角スペース


if __name__ == "__main__":
    unittest.main()
