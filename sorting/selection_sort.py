from generate import list


def selection_sort(l):
    for i in range(len(l)):
        min_idx = i
        for j in range(i + 1, len(l)):
            if l[min_idx] > l[j]:
                min_idx = j
        l[min_idx], l[i] = l[i], l[min_idx]
    return l


for i in range(100):
    test = list.generate_list(i)
    assert selection_sort(test) == sorted(test)