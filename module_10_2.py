from threading import Thread
from time import sleep

class Knight(Thread):
    number_of_enemies = 100
    number_of_battles = 0
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name} на нас напали!')
        while range(self.number_of_enemies):
            sleep(1)
            self.number_of_battles += 1
            self.number_of_enemies -= self.power
            print(f'{self.name} сражается {self.number_of_battles} дней(дня) осталось {self.number_of_enemies} воинов')
        return print(f'{self.name} одержал победу спустя {self.number_of_battles} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
thr1 = Thread(target=first_knight.run)
thr2 = Thread(target=second_knight.run)
thr1.start()
thr2.start()
thr1.join()
thr2.join()
print('Все битвы закончились!')