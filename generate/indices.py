def generate_indices(i, j, k):
    for i_ in range(i):
        for j_ in range(j):
            for k_ in range(k):
                yield (i_, j_, k_)