import time
import random
import os
number = "1"


# Функция, которая каждые 5 секунд генерит число-хекс в своём потоке
if __name__ == '__main__':
    while True:
        number = str(random.randint(100000, 999999))
        os.environ["NUMBER"] = number
        time.sleep(5.0)
        
       
