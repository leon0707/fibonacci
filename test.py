import unittest
from fibonacci_calculators import fib_dfs, fib_dp

class TestSum(unittest.TestCase):

    def test_fib_dfs(self):
        self.assertRaises(ValueError, fib_dfs, -1)
        self.assertEqual(fib_dfs(0), 0, "Should be 0")
        self.assertEqual(fib_dfs(1), 1, "Should be 1")
        self.assertEqual(fib_dfs(5), 5, "Should be 5")

    def test_fib_dp(self):
        self.assertRaises(ValueError, fib_dp, -1)
        self.assertEqual(fib_dp(0), 0, "Should be 0")
        self.assertEqual(fib_dp(1), 1, "Should be 1")
        self.assertEqual(fib_dp(5), 5, "Should be 5")

if __name__ == '__main__':
    unittest.main()