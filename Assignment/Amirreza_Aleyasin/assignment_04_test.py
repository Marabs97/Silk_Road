import unittest
from assignment_04 import decimal_to_binary_correct


class DecimalTestCase(unittest.TestCase):
    __doc__ = "check if the function decimal2binary works properly"

    def test_values(self):
        """Do values in the interval [-1,3] work?"""
        values = [-2, -1, 0, 1, 2, 3]
        for i in values:
            self.assertEqual(bin(i).replace("0b", "0"), decimal_to_binary_correct(i))

    if __name__ == '__main__':
        unittest.main()
