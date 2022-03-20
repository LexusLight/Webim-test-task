import time
import random
import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

cur = conn.cursor()

def create_table():
    commands = "CREATE TABLE numbers ( id SERIAL PRIMARY KEY, number VARCHAR(255))"
    cur.execute(commands)

    commands = "INSERT INTO numbers(id, number) VALUES(1, '777')"
    cur.execute(commands)

    print("Created!")

def update_number(num):
    query = "UPDATE numbers SET number={} WHERE id=1".format(num)

def get_number():
    query = "SELECT number FROM numbers WHERE id=1"

number = "1"

    # Функция, которая каждые 5 секунд генерит число-хекс в своём потоке
if __name__ == '__main__':
    create_table()
    while True:
        time.sleep(5.0)
        number = str(random.randint(100000, 999999))
