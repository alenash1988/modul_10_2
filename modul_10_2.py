import time
from threading import Thread

class Knight(Thread):
    def __init__(self, name, power):
        Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        day = 0
        n = 100
        print(f'{self.name}, на нас напали!')
        while n != 0:
            day += 1
            n -= self.power
            print(f'{self.name} сражается {day} дней(дня)..., осталось {n} воинов."')
            time.sleep(1)

        print(f'{self.name} одержал победу спустя {day} дней(дня)!')




first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print(f'Все битвы закончились!')


