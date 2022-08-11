def solution(a):
    aset = set()
    for i in a:
        if i in aset:
            return i
        else: 
            aset.add(i)    
    
    return -1

