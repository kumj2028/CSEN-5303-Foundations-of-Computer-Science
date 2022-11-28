import unittest
from multistack import MultiStack, StackFull, StackEmpty

class TestMultiStack(unittest.TestCase):
    # test creating a small multistack with one stack and array size of 5
    def test_small_single(self):
        ms = MultiStack(1, 5)
        self.assertEqual(ms.is_empty(0), True)
        with self.assertRaises(StackEmpty):
            ms.pop(0)
        ms.push(0, 3)
        self.assertEqual(ms.is_empty(0), False)
        self.assertEqual(ms.top(0), 3)
        ms.pop(0)
        self.assertEqual(ms.is_empty(0), True)
        ms.push(0, 3)
        ms.push(0, 1)
        ms.push(0, 4)
        ms.push(0, 1)
        ms.push(0, 5)
        with self.assertRaises(StackFull):
            ms.push(0, 9)
        self.assertEqual(ms.top(0), 5)
    
    #test creating default multistack with 3 stacks and array size of 20
    def test_default(self):
        ms = MultiStack()
        self.assertEqual(ms.is_empty(0), True)
        with self.assertRaises(StackEmpty):
            ms.pop(0)
        self.assertEqual(ms.is_empty(1), True)
        with self.assertRaises(StackEmpty):
            ms.pop(1)
        self.assertEqual(ms.is_empty(2), True)
        with self.assertRaises(StackEmpty):
            ms.pop(2)
        ms.push(0, 3)
        ms.push(0, 1)
        ms.push(0, 4)
        ms.push(0, 1)
        ms.push(0, 5)
        ms.push(1, 2)
        ms.push(1, 7)
        ms.push(1, 1)
        ms.push(1, 8)
        ms.push(2, 1)
        ms.push(2, 4)
        ms.push(2, 1)
        ms.push(2, 4)
        ms.push(2, 2)
        ms.push(2, 1)
        ms.push(2, 3)
        ms.push(2, 5)
        ms.push(2, 6)
        with self.assertRaises(StackFull):
            ms.push(2, 2)
        self.assertEqual(ms.top(0), 5)
        self.assertEqual(ms.top(1), 8)
        self.assertEqual(ms.top(2), 6)
        ms.pop(2)
        ms.pop(2)
        self.assertEqual(ms.top(2), 3)
        ms.push(0, 9)
        self.assertEqual(ms.top(0), 9)


if __name__ == '__main__':
    unittest.main()