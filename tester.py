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
    print(f"1 + 1 = 2? {tester.is_addition_true(1,1,2)}")
    print(f"5 + 1 = 5? {tester.is_addition_true(5,1,5)}")
    print(f"5 - 2 = 3? {tester.is_subtraction_true(5,2,3)}")
    print(f"1 - 1 = 1? {tester.is_subtraction_true(1,1,1)}")
