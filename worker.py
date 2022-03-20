import time
import random
import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()

def connect():
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()


def create_table():
    query = "CREATE TABLE numbers (id INTEGER PRIMARY KEY, number VARCHAR(255))"
    cur.execute(query)
    query = "INSERT INTO numbers(id, number) VALUES(1, '777')"
    cur.execute(query)
    print("Created!")
    print(get_number())

def update_number(num):
    query = "UPDATE numbers SET number={} WHERE id=1".format(num)

def get_number():
    query = "SELECT number FROM numbers WHERE id=1"
    cur.execute(query)
    num = cur.fetchall()
    num = num[0][0]
    return num

number = "1"

    # Функция, которая каждые 5 секунд генерит число-хекс в своём потоке
if __name__ == '__main__':
    connect()
    create_table()
    while True:
        time.sleep(5.0)
        number = str(random.randint(100000, 999999))
        update_number(number)
