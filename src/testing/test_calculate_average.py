# test_calculate_average.py
import unittest

from calculate_average import calculate_average

class TestCalculateAverage(unittest.TestCase):
    def setUp(self):
        self.marks = [80, 90, 70] # it is the entity that is used in everytest case

    def test_average_is_correct(self):
        self.assertEqual(calculate_average(self.marks), 80)

    def test_result_is_a_number(self):
        self.assertIsInstance(calculate_average(self.marks), float)

    def test_contains_expected_mark(self):
        self.assertIn(90, self.marks)

    def test_raises_on_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            calculate_average([])

if __name__ == "__main__":
    unittest.main()
