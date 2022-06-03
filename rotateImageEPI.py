def solution(a):
    matrix_size = len(a) - 1
    for i in range(len(a) // 2):
        for j in range(i, matrix_size - i):
            (a[i][j], a[~j][i], a[~i][~j], a[j][~i])= (a[~j][i], a[~i][~j], a[j][~i], a[i][j])
    return a
    

