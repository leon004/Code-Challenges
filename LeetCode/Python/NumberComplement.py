"""
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.
"""

class Solution:
    def findComplement(self, num: int) -> int:
        binary = list("{:b}".format(num)) #Convert the number into a list in binary format 
        
        for i in range(len(binary)):
            if binary[i] == "1":
                binary[i] = "0"
            else:
                binary[i] = "1"
                
        return int("".join(binary),base=2)    #Use the join method to create a string from a list 
