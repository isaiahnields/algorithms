from random import randint


def generate_list(n):
    res = list()
    for i in range(n):
        res.append(randint(0, n))
    return res
