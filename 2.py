import random
import time

class Ball:
    def __init__(self, number) -> None:
        self.number = number
        self.overweight = False

    def __str__(self) -> str:
        return f'{self.number} {self.overweight}; '
        

class LotteryMachine:
    def __init__(self) -> None:
        self.balls = []

        for i in range(1,50):
            self.balls.append(Ball(i))

        for i in random.sample(range(49), 6):
            self.balls[i].overweight = True

        self.running_status = False

    def start(self):
        if not self.running_status:
            print("Maszyna losujaca zaczyna dzialanie")
            self.running_status = True
        
    def stop(self):        
        if self.running_status:
            self.running_status = False

        print("Obecny stan listy kul")
        for ball in self.balls[:7]:
            print(ball)

    def shuffle(self):
        if self.running_status:
            balls_to_swap = random.sample(range(49), 2)
            # time.sleep(0.01)

            temp = self.balls[balls_to_swap[0]]
            self.balls[balls_to_swap[0]] = self.balls[balls_to_swap[1]]
            self.balls[balls_to_swap[1]] = temp

            for i in range(49):
                if self.balls[i].overweight and i != 0:
                    temp = self.balls[i]
                    self.balls[i] = self.balls[i - 1]
                    self.balls[i - 1] = temp

class LotteryPresenter:
    def main(self):
        print("Rozpoczynamy gre")
        shuffle_time = int(input("Podaj czas losowania: "))

        lottery_machine = LotteryMachine()
        start_time = time.time()

        lottery_machine.start()
        
        while start_time + shuffle_time < int(time.time()):
            lottery_machine.shuffle()
            time.sleep(0.01)

        lottery_machine.stop()

if __name__ == "__main__":
    lottery = LotteryPresenter()
    lottery.main()