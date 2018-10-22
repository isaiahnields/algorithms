from generate import list


def bubble_sort(l):
    for i in range(len(l)):
        sorted = True
        for j in range(len(l) - i - 1):
            if l[j] > l[j + 1]:
                sorted = False
                l[j], l[j + 1] = l[j + 1], l[j]
        if sorted: break
    return l


for i in range(100):
    test = list.generate_list(i)
    assert bubble_sort(test) == sorted(test)
