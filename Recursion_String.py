import unittest

'''
Write a recursive method that takes
1) a string to find
2) a string to replace the found string with,
3) an initial string. Return the initial string with all the found strings replaced with the replacement string.
    You may not use loops or the built-in string methods EXCEPT comparison, length, and slicing. Here is an outline.
'''

'''
Description: FIND AND REPLACE WORDS IN STRING THROUGH THE USE OF RECURSION
Author: DAREY LEE

'''


def findandreplace(find, replace, string):
    if string == "":
        return ("")

    if string == find:
        return replace

    if replace is None or find == "" or find is None:
        return string

    try:
        if string[:len(find)] == find:
            result = replace + findandreplace(find, replace, string[len(find):])

        else:
            result = string[:1] + findandreplace(find, replace, string[1:])

    except TypeError:
        return None

    return result

class TestFindAndReplace(unittest.TestCase):
    def test_all_none(self):
        self.assertEqual(findandreplace(None, None, None), None)

    def test_find_none(self):
        self.assertEqual(findandreplace(None, "a", "aabb"), "aabb")

    def test_find_empty(self):
        self.assertEqual(findandreplace("", "a", "aabb"), "aabb")

    def test_replace_none(self):
        self.assertEqual(findandreplace("a", None, "aabb"), "aabb")

    def test_string_none(self):
        self.assertEqual(findandreplace("a", "b", None), None)

    def test_simple(self):
        self.assertEqual(findandreplace("a", "b", "aabb"), "bbbb")

    def test_remove(self):
        self.assertEqual(findandreplace(" ", "", " a abb"), "aabb")

    def test_gettysburg(self):
        self.assertEqual(findandreplace("Four score", "Twenty", \
                                        "Four score and seven years ago"), "Twenty and seven years ago")

if __name__ == '__main__':
    unittest.main()