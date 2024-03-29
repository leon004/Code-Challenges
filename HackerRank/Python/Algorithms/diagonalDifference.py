"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix arr  is shown below:

1 2 3
4 5 6
9 8 9  

The left-to-right diagonal = 1 + 5 + 9 = 15. The right to left diagonal = 3 + 5 + 9 = 17. Their absolute difference is |15 - 17| = 2 


"""

def diagonalDifference(arr):
    d1 = sum([arr[i][i] for i in range(len(arr))])
    d2 = sum([arr[x][n - 1 - x] for x in range(len(arr))])
    return (abs(d1 - d2))
