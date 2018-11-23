from random import randint


def generate_list(n, gen=randint):
    for i in range(n): yield gen(0, n)