import time
import random

print("I AM WORKING2")
# Функция, которая каждые 5 секунд генерит число-хекс в своём потоке
if __name__ == '__main__':
    while True:
        print("I AM WORKING2")
        time.sleep(5.0)
        number = str(random.randint(100000, 999999))
        f = open('text.txt', 'w')
        f.write(number)
        f.close()
