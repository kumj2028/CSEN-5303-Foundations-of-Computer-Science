import unittest
from balanced_ternary import BalancedTernary

class TestBalancedTernary(unittest.TestCase):
    # test interval algorithm works for all numbers in range
    def test_interval(self):
        for i in range(-121, 122):
            interval_bt = BalancedTernary.decimal_to_balanced_ternary_interval(i)
            lookup_bt = BalancedTernary.lookup_table[i]
            self.assertEqual(interval_bt, lookup_bt)
    
    # test interval algorithm fails with ValueError when given number out of range
    def test_interval_out_of_range(self):
        with self.assertRaises(ValueError):
            BalancedTernary.decimal_to_balanced_ternary_interval(122)
    
    # test lookup algorithm fails with KeyError when given number out of range
    def test_lookup_out_of_range(self):
        with self.assertRaises(KeyError):
            BalancedTernary.lookup_table[122]

    # test ternary algorithm works for all numbers in range
    def test_ternary(self):
        for i in range(-121, 122):
            ternary_bt = BalancedTernary.decimal_to_balanced_ternary(i)
            lookup_bt = BalancedTernary.lookup_table[i]
            self.assertEqual(ternary_bt, lookup_bt)
    
    # test ternary algorithm still works for numbers outside interval range
    def test_ternary_out_of_range(self):
        ternary_bt = BalancedTernary.decimal_to_balanced_ternary(122)
        ground_truth_bt = [243, -81, -27, -9, -3, -1]
        self.assertEqual(ternary_bt, ground_truth_bt)

if __name__ == '__main__':
    unittest.main()