##################################################
# Imports
##################################################
import unittest
from unittest import TestCase

from src.halting.figures.numbers import ManageFigures

##################################################
# Manage Figures Test Case Implementation
##################################################

class ManageFiguresTestCase(TestCase):

    def setUp(self) -> None:
        self.figures = ManageFigures()
        return super().setUp()
    
    def test_calculate_number_of_significant_figures(self):
        self.assertEqual(self.figures.calculate_number_of_significant_figures('1200200'), 5)
        self.assertEqual(self.figures.calculate_number_of_significant_figures('345'), 3)
        self.assertEqual(self.figures.calculate_number_of_significant_figures('40005000600'), 9)
        self.assertEqual(self.figures.calculate_number_of_significant_figures('900040000'), 5)
        # test with decimals
        self.assertEqual(self.figures.calculate_number_of_significant_figures('0.001'), 1)
        self.assertEqual(self.figures.calculate_number_of_significant_figures('0.01020'), 4)
        self.assertEqual(self.figures.calculate_number_of_significant_figures('3223.100'), 7)
        self.assertEqual(self.figures.calculate_number_of_significant_figures('0.02920'), 4)

if __name__ == "__main__":
    unittest.main()
