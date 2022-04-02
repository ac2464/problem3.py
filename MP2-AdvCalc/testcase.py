import unittest
from is601.M7.AdvCalc import AdvCalc
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
        #home work date 02/19/2022 - ucid - ac2464
    def test_square(self):
        self.assertEqual(self.AdvCalc.square(2), 4)
        self.assertEqual(self.AdvCalc.square(3), 9)
        #home work date 02/19/2022 - ucid - ac2464
    def test_sqrt(self):
        self.assertEqual(self.AdvCalc.sqrt(2), 1.414213562)
        self.assertEqual(self.AdvCalc.sqrt(3), 1.732050808)
        #home work date 02/19/2022 - ucid - ac2464
    def test_mean(self):
        self.assertEqual(self.AdvCalc.mean([1, 2, 3, 4]), 2.5)
        self.assertEqual(self.AdvCalc.mean([-2, -3, -4, -5]), 3.5)
        #home work date 02/19/2022 - ucid - ac2464
    def test_median(self):
        self.assertEqual(self.AdvCalc.median([1, 3, 3, 4]), 3.0)
        self.assertEqual(self.AdvCalc.median([1, 2, 6, 4]), 3.0)
        #home work date 02/19/2022 - ucid - ac2464
    def test_mode(self):
        self.assertEqual(self.AdvCalc.mode([4, 5, 6, 7]), 4)
        self.assertEqual(self.AdvCalc.mode([1, 5, 8, 9]), 1)
        #home work date 02/19/2022 - ucid - ac2464
    def test_sd(self):
        self.assertEqual(self.AdvCalc.s_d([11, 22, 33, 44]), 12.29837388)
        self.assertEqual(self.AdvCalc.s_d([22, 33, 44, 55]), 12.29837388)
        #home work date 02/19/2022 - ucid - ac2464
    def test_v(self):
        self.assertEqual(self.AdvCalc.v([11, 2, 33, 4]), 201.66666666666666)
        self.assertEqual(self.AdvCalc.v([12, 33, 4, 55, 6]), 472.5)


if __name__ == '__main__':
    unittest.main()
