class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor  = x ^ y
        xor = "{:b}".format(xor)
        output = 0
        for i in xor:
            output += int(i)
        return output
 
#One Line Solution
# return sum([int(b) for b in "{:b}".format((x ^ y))])