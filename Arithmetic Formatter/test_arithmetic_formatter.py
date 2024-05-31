import unittest
from arithmetic_formatter import arithmetic_arranger

class TestArithmeticArranger(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(arithmetic_arranger(["3801 - 2", "123 + 49"]),
                         '  3801      123\n-    2    +  49\n------    -----')

        self.assertEqual(arithmetic_arranger(["1 + 2", "1 - 9380"]),
                         '  1         1\n+ 2    - 9380\n---    ------')

        self.assertEqual(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]),
                         '    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----')

        self.assertEqual(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]),
                         '  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------')

    def test_too_many_problems(self):
        self.assertEqual(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]),
                         'Error: Too many problems.')

    def test_invalid_operator(self):
        self.assertEqual(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]),
                         "Error: Operator must be '+' or '-'.")

    def test_number_too_large(self):
        self.assertEqual(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]),
                         'Error: Numbers cannot be more than four digits.')

    def test_non_digit_characters(self):
        self.assertEqual(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]),
                         'Error: Numbers must only contain digits.')

    def test_with_answers(self):
        self.assertEqual(arithmetic_arranger(["3 + 855", "988 + 40"], True),
                         '    3      988\n+ 855    +  40\n-----    -----\n  858     1028')

        self.assertEqual(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True),
                         '   32         1      45      123      988\n- 698    - 3801    + 43    +  49    +  40\n-----    ------    ----    -----    -----\n -666     -3800      88      172     1028')

if __name__ == '__main__':
    unittest.main()
