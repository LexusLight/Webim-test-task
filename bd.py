import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

cur = conn.cursor()

def create_table():
    commands = ("CREATE TABLE numbers ( id SERIAL PRIMARY KEY, number VARCHAR(255))",
                "INSERT INTO numbers(id, number) VALUES(1, 777)")
    cur.execute(commands)
    print("Created!")

def update_number(num):
    query = "UPDATE numbers SET number={} WHERE id=1".format(num)

def get_number():
    query = "SELECT number FROM numbers WHERE id=1"

if __name__ == '__main__':
    create_table()