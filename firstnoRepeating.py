from collections import Counter
def solution(s):
    freq = Counter(s)
    
    for i in s:
        if(freq[i] == 1):
            return i
            break
        
    return '_'
        

