from unittest import TestCase, main
from math import sum


class TestSum(TestCase):
    def test_integers(self):
        self.assertEqual(sum(2, 5), 7)
        self.assertEqual(sum(3, 3), 8)


if __name__ == '__main__':
    main()
