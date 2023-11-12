import threading
import time
import random

class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def is_alive(self):
        return self.health > 0

    def attack(self, other):
        time.sleep(random.randint(1, 3))
        while self.is_alive() and other.is_alive():
              # случайная задержка
            if other.is_alive():
                other.health -= 20
                print(f"{self.name} бьет {other.name} - У {other.name} осталось {other.health}")
            time.sleep(random.randint(1, 3))
        if other.health <= 0:
            print(f"{self.name} одержал победу!")
            return

# Создаем двух воинов
warrior1 = Warrior("Первый")
warrior2 = Warrior("Второй")

# Создаем потоки для каждого воина
thread1 = threading.Thread(target=warrior1.attack, args=(warrior2,))
thread2 = threading.Thread(target=warrior2.attack, args=(warrior1,))

# Запускаем потоки
thread2.start()
thread1.start()

# Ожидаем завершения обоих потоков
thread1.join()
thread2.join()