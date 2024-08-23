def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print('Matrix:')
    for g in range(n):
        print(matrix[g])
get_matrix(3,4,22)