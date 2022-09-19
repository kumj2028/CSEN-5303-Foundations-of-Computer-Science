import unittest
import filecmp
from cell_map import cellmap

class TestCellMap(unittest.TestCase):
    # empty cellmap will not change in the next generation
    def test_empty(self):
        current_map = cellmap(3, 3, file='tests/empty.txt')
        next_map = current_map.next_generation()
        next_map.write_to_file('tests/next.txt')
        self.assertTrue(filecmp.cmp('tests/empty.txt', 'tests/next.txt'))
    
    # cellmap with a 2x2 square will not change in the next generation
    def test_square(self):
        current_map = cellmap(3, 3, file='tests/square.txt')
        next_map = current_map.next_generation()
        next_map.write_to_file('tests/next.txt')
        self.assertTrue(filecmp.cmp('tests/square.txt', 'tests/next.txt'))

    # cellmap with a 1x3 horizontal line will change to a 3x1 vertical line
    def test_horizontal(self):
        current_map = cellmap(3, 3, file='tests/horizontal.txt')
        next_map = current_map.next_generation()
        next_map.write_to_file('tests/next.txt')
        self.assertTrue(filecmp.cmp('tests/vertical.txt', 'tests/next.txt'))

    # cellmap with a 3x1 vertical line will change to a 1x3 horizontal line
    def test_vertical(self):
        current_map = cellmap(3, 3, file='tests/vertical.txt')
        next_map = current_map.next_generation()
        next_map.write_to_file('tests/next.txt')
        self.assertTrue(filecmp.cmp('tests/horizontal.txt', 'tests/next.txt'))

    # a glider in the top left corner of a 5x5 matrix
    # will glide down to the bottom right corner and become a square
    def test_glider(self):
        current_map = cellmap(5,5, file='tests/glider0.txt')
        next_map = current_map.next_generation()
        next_map.write_to_file('tests/next.txt')
        for i in range(1, 11):
            self.assertTrue(filecmp.cmp(f'tests/glider{i}.txt', 'tests/next.txt'))
            next_map = next_map.next_generation()
            next_map.write_to_file('tests/next.txt')
        self.assertTrue(filecmp.cmp('tests/square2.txt', 'tests/next.txt'))

unittest.main()