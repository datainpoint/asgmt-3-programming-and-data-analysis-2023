import unittest
import importlib

class TestAssignmentThree(unittest.TestCase):
    def test_01_sort_list_with_ascending_order(self):
        self.assertEqual(asgmt.sort_list_with_ascending_order([6, 6, 5, 5]),
                         [5, 5, 6, 6])
        self.assertEqual(asgmt.sort_list_with_ascending_order([3, 2, 1]),
                         [1, 2, 3])
        self.assertEqual(asgmt.sort_list_with_ascending_order([2, 5, 3]),
                         [2, 3, 5])
        self.assertEqual(asgmt.sort_list_with_ascending_order([2, 5, 3, 11, 7]),
                         [2, 3, 5, 7, 11])
        self.assertEqual(asgmt.sort_list_with_ascending_order([11, 7, 5, 3, 2]),
                         [2, 3, 5, 7, 11])
    def test_02_sort_list_with_descending_order(self):
        self.assertEqual(asgmt.sort_list_with_descending_order([5, 5, 6, 6]),
                         [6, 6, 5, 5])
        self.assertEqual(asgmt.sort_list_with_descending_order([1, 2, 3]),
                         [3, 2, 1])
        self.assertEqual(asgmt.sort_list_with_descending_order([2, 5, 3]),
                         [5, 3, 2])
        self.assertEqual(asgmt.sort_list_with_descending_order([2, 5, 3, 11, 7]),
                         [11, 7, 5, 3, 2])
        self.assertEqual(asgmt.sort_list_with_descending_order([2, 3, 5, 7, 11]),
                         [11, 7, 5, 3, 2])
    def test_03_return_integer_with_fizz_buzz_rule(self):
        self.assertEqual(asgmt.return_integer_with_fizz_buzz_rule(1), 1)
        self.assertEqual(asgmt.return_integer_with_fizz_buzz_rule(2), 2)
        self.assertEqual(asgmt.return_integer_with_fizz_buzz_rule(3), 'Fizz')
        self.assertEqual(asgmt.return_integer_with_fizz_buzz_rule(5), 'Buzz')
        self.assertEqual(asgmt.return_integer_with_fizz_buzz_rule(15), 'Fizz Buzz')
        self.assertEqual(asgmt.return_integer_with_fizz_buzz_rule(16), 16)
        self.assertEqual(asgmt.return_integer_with_fizz_buzz_rule(17), 17)
    def test_04_return_first_n_fizz_buzz(self):
        self.assertEqual(asgmt.return_first_n_fizz_buzz(2),
                         [1, 2])
        self.assertEqual(asgmt.return_first_n_fizz_buzz(3),
                         [1, 2, 'Fizz'])
        self.assertEqual(asgmt.return_first_n_fizz_buzz(4),
                         [1, 2, 'Fizz', 4])
        self.assertEqual(asgmt.return_first_n_fizz_buzz(6),
                         [1, 2, 'Fizz', 4, 'Buzz', 'Fizz'])
        self.assertEqual(asgmt.return_first_n_fizz_buzz(15),
                         [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz Buzz'])
    def test_05_range_fizz_buzz(self):
        self.assertEqual(asgmt.range_fizz_buzz(1, 5), [1, 2, 'Fizz', 4])
        self.assertEqual(asgmt.range_fizz_buzz(3, 5), ['Fizz', 4])
        self.assertEqual(asgmt.range_fizz_buzz(1, 6), [1, 2, 'Fizz', 4, 'Buzz'])
        self.assertEqual(asgmt.range_fizz_buzz(3, 6), ['Fizz', 4, 'Buzz'])
        self.assertEqual(asgmt.range_fizz_buzz(1, 16), 
                         [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz Buzz'])
        self.assertEqual(asgmt.range_fizz_buzz(13, 16), [13, 14, 'Fizz Buzz'])
    def test_06_retrieve_middle_elements(self):
        self.assertEqual(asgmt.retrieve_middle_elements([2, 3, 5]), 3)
        self.assertEqual(asgmt.retrieve_middle_elements([2, 3, 5, 7]), (3, 5))
        self.assertEqual(asgmt.retrieve_middle_elements([2, 3, 5, 7, 11]), 5)
        self.assertEqual(asgmt.retrieve_middle_elements([2, 3, 5, 7, 11, 13]), (5, 7))
        self.assertEqual(asgmt.retrieve_middle_elements([2, 3, 5, 7, 11, 13, 17]), 7)
        self.assertEqual(asgmt.retrieve_middle_elements([2, 3, 5, 7, 11, 13, 17, 19]), (7, 11))
    def test_07_median(self):
        self.assertEqual(asgmt.median([2, 3, 5]), 3)
        self.assertEqual(asgmt.median([2, 3, 5, 7, 11]), 5)
        self.assertEqual(asgmt.median([2, 3, 5, 7, 11, 13]), 6.0)
        self.assertEqual(asgmt.median([11, 13, 17, 2, 3, 5, 7]), 7)
        self.assertEqual(asgmt.median([7, 11, 13, 17, 19, 2, 3, 5]), 9.0)
    def test_08_collect_divisors(self):
        self.assertEqual(asgmt.collect_divisors(1), [1])
        self.assertEqual(asgmt.collect_divisors(2), [1, 2])
        self.assertEqual(asgmt.collect_divisors(3), [1, 3])
        self.assertEqual(asgmt.collect_divisors(4), [1, 2, 4])
        self.assertEqual(asgmt.collect_divisors(5), [1, 5])
        self.assertEqual(asgmt.collect_divisors(6), [1, 2, 3, 6])
        self.assertEqual(asgmt.collect_divisors(7), [1, 7])
    def test_09_is_prime(self):
        self.assertFalse(asgmt.is_prime(1))
        self.assertTrue(asgmt.is_prime(2))
        self.assertTrue(asgmt.is_prime(3))
        self.assertFalse(asgmt.is_prime(4))
        self.assertTrue(asgmt.is_prime(5))
        self.assertFalse(asgmt.is_prime(6))
        self.assertTrue(asgmt.is_prime(7))
    def test_10_filter_primes_within_range(self):
        self.assertEqual(asgmt.filter_primes_within_range(1, 5), [2, 3])
        self.assertEqual(asgmt.filter_primes_within_range(6, 10), [7])
        self.assertEqual(asgmt.filter_primes_within_range(11, 15), [11, 13])
        self.assertEqual(asgmt.filter_primes_within_range(16, 20), [17, 19])
        self.assertEqual(asgmt.filter_primes_within_range(21, 25), [23])
        self.assertEqual(asgmt.filter_primes_within_range(26, 30), [29])
        self.assertEqual(asgmt.filter_primes_within_range(31, 35), [31])

asgmt = importlib.import_module("asgmt-three")
suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentThree)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print("You've got {} successes among {} questions.".format(number_of_successes, number_of_test_runs))