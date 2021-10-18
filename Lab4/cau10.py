def sparse_dot(vector_a, vector_b):
    multiplication = 0
    for key1 in vector_a:
        if key1 in vector_b:
            multiplication = multiplication + vector_a[key1] * vector_b[key1]
    return multiplication
print(sparse_dot({1: 3, 2: 3, 3: 4}, {2: 4, 3: 5, 4: 6}))