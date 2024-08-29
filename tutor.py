from random import randint
from tester import Tester


class Tutor:
    DEFAULT_ROUNDS = 10

    def __init__(self) -> None:
        self.tester = Tester()
        self.score = 0.0
        self.run_time = 0

    def run(self) -> None:
        print("Running tutor.py")
        is_running = True
        while is_running:
            res = input("Would you like to practice addition (y/n)? ")
            if res == 'y':
                self.run_time += 1
                res = input("How many rounds would you like to play (defaults to 10)? ")
                try:
                    rounds = int(res)
                except:
                    rounds = self.DEFAULT_ROUNDS
                res = input("What's the maximum number? ")
                try:
                    max_num = int(res)
                except:
                    max_num = self.DEFAULT_ROUNDS
                correct = self._playAddition(rounds, max_num)
                self._calculateScore(correct,rounds)
            res = input("Do you want to play again (y/n)? ")
            if res == 'n':
                print(f"Thanks for playing for {self.run_time} runs!")
                is_running = False
    
    def _calculateScore(self, correct: int, rounds: int=DEFAULT_ROUNDS) -> None:
        print(f"You got {correct} numbers out of {rounds}.")
        added_score = (correct/rounds)*100
        print(f"This is {added_score}% accuracy.")
        sub = self.score + added_score
        self.score = sub / self.run_time
        print(f"All time accuracy from {self.run_time} runs is {self.score}%")

    def _playAddition(self, rounds: int=DEFAULT_ROUNDS, max_num: int=DEFAULT_ROUNDS) -> int:
        temp_score = 0
        for _ in range(rounds):
            num1 = randint(1,max_num)
            num2 = randint(1,max_num)
            res_str = input(f"{num1} + {num2} = ")
            is_correct = False
            try:
                res = int(res_str)
                is_correct = self.tester.is_addition_true(num1,num2,res)
            except:
                pass
            if is_correct:
                temp_score += 1
        return temp_score


if __name__ == '__main__':
    app = Tutor()
    app.run()
