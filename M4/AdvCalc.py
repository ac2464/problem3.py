import math
import statistics
import numpy as np
import scipy.stats as st
class AdvCalc:
    ans = 0

    def _is_float(self, val):
        try:
            val = float(val)
            return True
        except:
            return False

    def _is_int(self, val):
        try:
            val = int(val)
            return True
        except:
            return False

    def _as_number(self, val):
        if self._is_int(val):
            return int(val)
        elif self._is_float(val):
            return float(val)
        elif isinstance(val, list):
            return list(val)
        else:
            raise Exception(" its Not a number")
# Ucid = ap2725 date = 02/17/22
    def add(self, num1, num2):
        if num1 == "ans":
            return self.add(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1 + num2
        return self.ans
# Ucid = ap2725 date = 02/17/22
    def sub(self, num1, num2):
        if num1 == "ans":
            return self.sub(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1 - num2
        return self.ans
# Ucid = ap2725 date = 02/17/22
    def mult(self, num1, num2):
        if num1 == "ans":
            return self.mult(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1 * num2
        return self.ans
# Ucid = ap2725 date = 02/17/22
    def div(self, num1, num2):
        if num1 == "ans":
            return self.div(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            if num2 == 0:
                print("Cannot divide by zero")
            else:
                self.ans = round((num1 / num2), 9)
        return self.ans

    def square(self, num1):
        num1 = self._as_number(num1)
        self.ans = pow(num1, 2)
        return self.ans

    def squareroot(self, num1):
        num1 = self._as_number(num1)
        sq = math.sqrt(num1)
        self.ans = float('%.20' % sq)
        return self.ans
# Ucid = ap2725 date = 03/07/22
    def mean(self, num1):
        # Ucid = ap2725 date = 03/07/22
        num1 = self._as_number(num1)
        self.ans = statistics.mean(num1)
        return self.ans
    # Ucid = ap2725 date = 03/07/22
    def median(self, num1):
        num1 = self._as_number(num1)
        self.ans = statistics.median(num1)
        return self.ans
    # Ucid = ap2725 date = 03/07/22
    def mode(self, num1):
        num1 = self._as_number(num1)
        self.ans = statistics.mode(num1)
        return self.ans
    # Ucid = ap2725 date = 03/07/22
    def standard_deviation(self, num1):
        num1 = self._as_number(num1)
        psd = statistics.pstdev(num1)
        self.ans = round(psd, 8)
        return self.ans
    def pv(self, num1):
        num1 = self._as_number(num1)
        self.ans = statistics.variance(num1)
        return self.ans
if __name__ == '__main__':
    is_running = True
    iSTR = input("Are you ready?")
    calc = AdvCalc()
    print(calc)
    if iSTR == "yes":
        while is_running:
            print(" Use sq for square and sr for square root ")
            iSTR = input("What is your eq:")
            if iSTR == "quit" or iSTR == "q":
                is_running = False
            else:
                print("Your eq was " + str(iSTR))
                if "+" in iSTR:
                    nums = iSTR.split("+")
                    r = calc.add(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))
                elif "-" in iSTR:
                    nums = iSTR.split("-")
                    r = calc.sub(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))
                elif "*" in iSTR or "x" in iSTR:
                    nums = iSTR.split("*") if "*" in iSTR else iSTR.split("x")
                    r = calc.mult(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))
                elif "/" in iSTR:
                    nums = iSTR.split("/")
                    r = calc.div(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))
                elif "square" in iSTR:
                    nums = iSTR.split("square")
                    r = calc.squ(nums[0].strip())
                    print("R is " + str(r))
                elif "squareroot" in iSTR:
                    nums = iSTR.split("squareroot")
                    r = calc.sr(nums[0].strip())
                    print("R is " + str(r))
                elif "men" in iSTR:
                    nums = iSTR.split("men")
                    nums = nums[0].split(' ')
                    for i in range(len(nums)):
                        nums[i] = int(nums[i])
                    print(nums)
                    r = calc.men(nums)
                    print("R is " + str(r))
                elif "med" in iSTR:
                    nums = iSTR.split("med")
                    nums = nums[0].split(' ')
                    for i in range(len(nums)):
                        nums[i] = int(nums[i])
                    print(nums)
                    r = calc.med(nums)
                    print("R is " + str(r))
                elif "mod" in iSTR:
                    nums = iSTR.split("mod")
                    nums = nums[0].split(' ')
                    for i in range(len(nums)):
                        nums[i] = int(nums[i])
                    print(nums)
                    r = calc.mod(nums)
                    print("R is " + str(r))
                elif "pv" in iSTR:
                    nums = iSTR.split("pv")
                    nums = nums[0].split(' ')
                    for i in range(len(nums)):
                        nums[i] = int(nums[i])
                    print(nums)
                    r = calc.pv(nums)
                    print("R is " + str(r))
                elif "posd" in iSTR:
                    nums = iSTR.split("posd")
                    nums = nums[0].split(' ')
                    for j in range(len(nums)):
                        nums[j] = int(nums[j])
                    print(nums)
                    r = calc.posd(nums)
                    print("R is " + str(r))

    else:
        print("Good bye")
        is_running = False
