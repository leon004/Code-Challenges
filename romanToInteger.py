class Solution:
    def romanToInt(self, s: str) -> int:
         romVal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
         intVal = 0
         for i in range(len(s)):
            if i > 0 and romVal[s[i]] > romVal[s[i-1]]:
                intVal += romVal[s[i]] - 2 * romVal[s[i-1]]
            else: 
                intVal += romVal[s[i]]
            
         return intVal
        
        