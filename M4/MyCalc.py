#home work date 02/19/2022 - ucid - ac2464
class MyCalc:
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
        else:
            raise Exception("Not a number")



    def add(self, number1, number2):
        if number1 == "ans":
            return self.add(self.ans, number2)
        else:
            number1 = self._as_number(number1)
            number2 = self._as_number(number2)
            self.ans = number1+number2
        return self.ans
    #home work date 02/19/2022 - ucid - ac2464
    def sub(self, number1, number2):
        if number1 == "ans":
            return self.sub(self.ans, number2)
        else:
            number1 = self._as_number(number1)
            number2 = self._as_number(number2)
            self.ans = number1-number2
        return self.ans
#home work date 02/19/2022 - ucid - ac2464
    def mult(self, number1, number2):
        if number1 == "ans":
            return self.mult(self.ans, number2)
        else:
            number1 = self._as_number(number1)
            number2 = self._as_number(number2)
            self.ans = number1*number2
        return self.ans
#home work date 02/19/2022 - ucid - ac2464
    def div(self, number1, number2):
        if number1 == "ans":
            return self.div(self.ans, number2)
        else:
            number1 = self._as_number(number1)
            number2 = self._as_number(number2)
            if number2 == 0:
                print("Can't divide by zero, sorry")
            else:
                self.ans = number1/number2
        return self.ans


if __name__ == '__main__':
    is_running = True
    iSTR = input("Are you ready?")
    calc = MyCalc()
    print(calc)
    if iSTR == "yes":
        while is_running:
            iSTR = input("What is your eq:")
            if iSTR == "quit" or iSTR == "q":
                is_running = False
            else:
                print("Your eq was " + str(iSTR))
                if "+" in iSTR:
                    nums = iSTR.split("+")
                    r = calc.add(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))
                elif "/" in iSTR:
                    nums = iSTR.split("/")
                    r = calc.div(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))

                elif "*" in iSTR or "x" in iSTR:
                    nums = iSTR.split("*") if "*" in iSTR else iSTR.split("x")
                    r = calc.mult(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))
                elif "-" in iSTR:
                    nums = iSTR.split("-")
                    r = calc.sub(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))




    else:
        print("adios")
        is_running = False
