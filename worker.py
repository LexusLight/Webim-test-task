import time
import random


# Тут был код для работы с Redis. Redis хероку мне не дал юзнуть, тк аддон не добаляется в рашке.
# Обмен числом через файлик хероку сделать не дала (ReadOnly политика)


number = "1"

# Функция, которая каждые 5 секунд генерит число-хекс в своём потоке
if __name__ == '__main__':
    while True:
        time.sleep(5.0)
        number = str(random.randint(100000, 999999))