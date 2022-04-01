import unittest
from AdvCalc import AdvCalc
class Testing(unittest.TestCase):
    def setUp(self):
        self.AdvCalc = AdvCalc()
        #home work date 02/19/2022 - ucid - ac2464
    def test_add(self):
        self.assertEqual(self.AdvCalc.add(10, 5), 15)
        self.assertEqual(self.AdvCalc.add("ans", 5), 20)
        #home work date 02/19/2022 - ucid - ac2464
    def test_mull(self):
        self.assertEqual(self.AdvCalc.mult(2, 4), 8)
        self.assertEqual(self.AdvCalc.mult("ans", 6), 48)
        #home work date 02/19/2022 - ucid - ac2464
    def test_sub(self):
        self.assertEqual(self.AdvCalc.sub(2, 0), 2)
        self.assertEqual(self.AdvCalc.sub("ans", 2), 0)
        #home work date 02/19/2022 - ucid - ac2464
    def test_div(self):
        self.assertEqual(self.AdvCalc.div(4, 2), 2)
        self.assertEqual(self.AdvCalc.div("ans", 2), 1)
    def test_square(self):
        self.assertEqual(self.AdvCalc.sq(2), 4)
        self.assertEqual(self.AdvCalc.squ(3), 9)
if __name__ == '__main__':
    unittest.main()
