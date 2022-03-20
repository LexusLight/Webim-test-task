import time
import random
import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

number = "1"

    # Функция, которая каждые 5 секунд генерит число-хекс в своём потоке
if __name__ == '__main__':
    while True:
        time.sleep(5.0)
        number = str(random.randint(100000, 999999))
