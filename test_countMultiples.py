import unittest
from testrun import countMultiples


class TestCountMultiples(unittest.TestCase):
    """Test values taken from original SingPath exercise Python >> Level 4 >>Count Multiple"""

    def test1(self):
        self.assertEqual(countMultiples([3, 5], 100), 46)

    def test2(self):
        self.assertEqual(countMultiples([3, 5, 7], 30), 16)

    def test3(self):
        self.assertEqual(countMultiples([3], 30), 9)

    def test4(self):
        self.assertEqual(countMultiples([13, 25], 100250), 11412)

    def test5(self):
        self.assertEqual(countMultiples([13, 35, 47], 389560), 47673)

    def test6(self):
        self.assertEqual(countMultiples([3], 389750), 129916)

if __name__ == '__main__':

    unittest.main()
