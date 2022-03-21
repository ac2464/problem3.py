import unittest
from MyCalc import MyCalc
class Testing(unittest.TestCase):
    def setUp(self):
        self.MyCalc = MyCalc()
        #home work date 02/19/2022 - ucid - ac2464
    def test_add(self):
        self.assertEqual(self.MyCalc.add(10, 5), 15)
        self.assertEqual(self.MyCalc.add("ans", 5), 20)
        #home work date 02/19/2022 - ucid - ac2464
    def test_mull(self):
        self.assertEqual(self.MyCalc.mult(2, 4), 8)
        self.assertEqual(self.MyCalc.mult("ans", 6), 48)
        #home work date 02/19/2022 - ucid - ac2464
    def test_sub(self):
        self.assertEqual(self.MyCalc.sub(2, 0), 2)
        self.assertEqual(self.MyCalc.sub("ans", 2), 0)
        #home work date 02/19/2022 - ucid - ac2464
    def test_div(self):
        self.assertEqual(self.MyCalc.div(4, 2), 2)
        self.assertEqual(self.MyCalc.div("ans", 2), 1)
if __name__ == '__main__':
    unittest.main()

        




