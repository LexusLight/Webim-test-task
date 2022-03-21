import os
import random
import time

def random_number():
    while True:
        number = random.randint(100000, 999999)
        f = open("file.txt","w")
        f.write(str(number))
        f.close()
        time.sleep(5.0)


if __name__ == "__main__":
    random_number()