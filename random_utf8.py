import random


def utf8_length():
    b = bytearray()
    try:
        while True:
            b.append(random.randrange(256))
            if b[-1] < 128:
                 b.decode()
    except UnicodeDecodeError:
        return len(b) - 1
