import time
import random


# Функция, которая каждые 5 секунд генерит число-хекс в своём потоке
if __name__ == '__main__':
    while True:
        time.sleep(5.0)
        number = str(random.randint(100000, 999999))
        f = open('text.txt', 'w')
        f.write(number)
