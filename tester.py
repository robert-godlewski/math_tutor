class Tester:
    def is_addition_true(self, num1: int, num2: int, res: int) -> bool:
        if res == num1+num2:
            return True
        else:
            return False

    def is_subtraction_true(self, num1: int, num2: int, res: int) -> bool:
        if res == num1-num2:
            return True
        else:
            return False

    def is_multiplication_true(self, num1: int, num2: int, res: int) -> bool:
        if res == num1*num2:
            return True
        else:
            return False

    def is_division_true(self, num1: int, num2: int, res: int) -> bool:
        if res == num1/num2:
            return True
        else:
            return False


if __name__ == '__main__':
    print("Running tester.py")
    tester = Tester()
    print(tester.is_addition_true(1,1,2))
    print(tester.is_addition_true(5,1,5))
