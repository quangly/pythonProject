import main
import unittest


class TestMain(unittest.TestCase):

    def test_isSubstring(self):
        s1 = "for"
        s2 = "geeksforgeeks"
        res = main.isSubstring(s2, s1)
        self.assertEqual(res, 5, "Should be 5")

    def test_isSubstring2(self):
        s1 = "ams"
        s2 = "deltadreams"
        res = main.isSubstring(s2, s1)
        self.assertEqual(res, 7, "Should be 7")

    def test_isPalindrome(self):
        s1 = "racecar"
        res = main.isPalindrome(s1)
        self.assertEqual(res, True)


if __name__ == "__main__":
    unittest.main()

