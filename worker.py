import time
import random

number = ""


# Функция, которая каждые 5 секунд генерит число-хекс в своём потоке
if __name__ == '__main__':
    while True:
        global number
        print("NEW NUMBER " + number)
        time.sleep(5.0)
        number = str(random.randint(100000, 999999))
        
