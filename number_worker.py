import time
import random


# Функция, которая каждые 5 секунд генерит число-хекс в своём потоке
from threading import Thread
while True:
    global number
    time.sleep(5.0)
    number = str(random.randint(100000, 999999))
    f = open('text.txt', 'w')
    f.write(number)

