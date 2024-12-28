import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies_remaining = 100
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")

        max_days = (self.enemies_remaining + self.power - 1) // self.power

        for day in range(1, max_days + 1):
            time.sleep(1)
            self.days = day
            self.enemies_remaining -= self.power
            if self.enemies_remaining < 0:
                self.enemies_remaining = 0

            print(f"{self.name}, сражается {self.days} день(дня)..., осталось {self.enemies_remaining} воинов.")
            if self.enemies_remaining == 0:
                break

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")
