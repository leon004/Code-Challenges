"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with 6 places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, 
though answers with absolute error of up to 10^4 are acceptable.

"""

def plusMinus(arr):
     maj,men,zero = 0
    total = len(arr)
    for i in range(len(arr)):
        if ((arr[i]) > 0):
            maj += 1
        elif ((arr[i]) == 0):
            zero = zero + 1
        elif ((arr[i]) < 0):
            men +=1
    res1 = maj / total
    res2 = men / total
    res3 = zero / total
    print(res1)
    print(res2)
    print(res3)